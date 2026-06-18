#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render_parts.py — Renderiza una imagen por pieza fabricada del CAD maestro.

Fuente de identidad: objetos del .3dm agrupados por capa (hoja).
Estrategia:
  - Extrusiones -> GetMesh(MeshType.Any) (identidad exacta).
  - Breps -> BrepFace.GetMesh() por cara; se combinan (identidad exacta por cara).
  - Si una pieza no aporta malla, se reporta en el manifiesto como VER CAD.

Nota sobre gmsh/OCC:
  Se carga el STEP en gmsh para diagnosticar entidades, validar la envolvente global
  y contrastar el conteo con los objetos Rhino. El mallado OCC del modelo completo
  falla con "overlapping facets"; por eso el render final se hace desde las mallas
  nativas de rhino3dm, preservando la identidad de cada objeto.

Salidas:
  docs/img/piezas/<slug>.png       — una por pieza fabricada.
  docs/img/piezas/_conjunto.png    — vista isometrica de todas las piezas juntas.
  docs/img/piezas/manifiesto.md    — resumen legible.
  docs/img/piezas/manifiesto.json  — resumen maquina.
"""

import json
import math
import os
import re
import sys
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.colors import LightSource, to_rgba_array
import numpy as np
import rhino3dm

# --------------------------------------------------------------------------- #
# gmsh: requerido al menos para el diagnostico; el script aborta si falta.
# --------------------------------------------------------------------------- #
try:
    import gmsh
    HAS_GMSH = True
except Exception as exc:  # pragma: no cover
    HAS_GMSH = False
    GMSH_IMPORT_ERROR = str(exc)


# --------------------------------------------------------------------------- #
# Paths
# --------------------------------------------------------------------------- #
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
REDISENO = HERE
CAD_DIR = os.path.join(REDISENO, "cad")
MODEL_3DM = os.path.join(REDISENO, "Incubadora-Final.3dm")
MODEL_STP = os.path.join(REDISENO, "Incubadora-Final.stp")
MODEL_IGS = os.path.join(REDISENO, "Incubadora-Final.igs")
OUT_DIR = os.path.join(REPO, "docs", "img", "piezas")

EXPECTED_ENVELOPE_MM = (605.0, 1264.0, 1189.0)
BBOX_TOLERANCE = 0.20


# --------------------------------------------------------------------------- #
# Utilidades
# --------------------------------------------------------------------------- #
def slugify(name: str) -> str:
    """Slug seguro para nombre de archivo."""
    s = name.lower().strip().replace(" ", "-").replace("/", "-").replace(":", "-")
    s = re.sub(r"[^a-z0-9_-]+", "", s)
    return s or "pieza"


def safe_finally(finalizer):
    """Ejecuta finalizer ignorando errores."""
    try:
        finalizer()
    except Exception:
        pass


# --------------------------------------------------------------------------- #
# Inventario y objetos Rhino
# --------------------------------------------------------------------------- #
def load_inventory():
    """Carga inventario.json y devuelve solo piezas a renderizar."""
    path = os.path.join(CAD_DIR, "inventario.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    target = [
        r for r in data["piezas"]
        if r["categoria"] != "visual" and r["fabricacion"] != "comprar"
    ]
    return target


def build_layer_index(model):
    """Devuelve {layer_index: (ruta_completa, nombre_hoja)}."""
    layers = list(model.Layers)
    by_id = {str(l.Id): l for l in layers}
    NULL_GUID = "00000000-0000-0000-0000-000000000000"
    out = {}
    for i, l in enumerate(layers):
        parts = [l.Name]
        pid = str(l.ParentLayerId)
        seen = set()
        while pid and pid != NULL_GUID and pid not in seen:
            seen.add(pid)
            p = by_id.get(pid)
            if not p:
                break
            parts.insert(0, p.Name)
            pid = str(p.ParentLayerId)
        out[i] = ("::".join(parts), l.Name)
    return out


def load_rhino_objects(model_path: str):
    """Lee el .3dm y devuelve lista de objetos con capa, centroide, bbox y geometria."""
    if not os.path.exists(model_path):
        raise SystemExit(f"No se encontro el CAD maestro: {model_path}")
    model = rhino3dm.File3dm.Read(model_path)
    layer_idx = build_layer_index(model)
    objs = []
    for obj in model.Objects:
        attr = obj.Attributes
        geom = obj.Geometry
        path, leaf = layer_idx.get(attr.LayerIndex, ("?", "?"))
        bb = geom.GetBoundingBox()
        centroid = (
            (bb.Min.X + bb.Max.X) / 2.0,
            (bb.Min.Y + bb.Max.Y) / 2.0,
            (bb.Min.Z + bb.Max.Z) / 2.0,
        )
        objs.append({
            "path": path,
            "leaf": leaf,
            "centroid": centroid,
            "bbox": (bb.Min.X, bb.Min.Y, bb.Min.Z, bb.Max.X, bb.Max.Y, bb.Max.Z),
            "geom": geom,
            "type": type(geom).__name__,
        })
    return objs


# --------------------------------------------------------------------------- #
# gmsh / OCC: solo diagnostico y validacion
# --------------------------------------------------------------------------- #
def gmsh_diagnostic():
    """Carga STEP en gmsh, reporta entidades y valida envolvente. Retorna dict."""
    if not HAS_GMSH:
        return {
            "ok": False,
            "source": "ninguno",
            "entities_3d": 0,
            "entities_2d": 0,
            "bbox_mm": None,
            "centroid_match": None,
            "note": f"gmsh no disponible: {GMSH_IMPORT_ERROR}",
        }

    source = None
    for candidate, label in ((MODEL_STP, "stp"), (MODEL_IGS, "igs")):
        if not os.path.exists(candidate):
            continue
        gmsh.initialize()
        gmsh.option.setNumber("General.Terminal", 0)
        try:
            gmsh.open(candidate)
            source = label
            break
        except Exception as exc:
            safe_finally(gmsh.finalize)
            last_err = str(exc)
    if source is None:
        return {
            "ok": False,
            "source": "ninguno",
            "entities_3d": 0,
            "entities_2d": 0,
            "bbox_mm": None,
            "centroid_match": None,
            "note": "No se pudo abrir ni .stp ni .igs con gmsh/OCC",
        }

    try:
        e3 = gmsh.model.getEntities(3)
        e2 = gmsh.model.getEntities(2)
        bb = gmsh.model.getBoundingBox(-1, -1)
        bbox = (bb[3] - bb[0], bb[4] - bb[1], bb[5] - bb[2])

        # Validacion de envolvente
        ok = True
        note_parts = []
        for i, (dim, name) in enumerate(zip(bbox, ("ancho", "prof", "alto"))):
            exp = EXPECTED_ENVELOPE_MM[i]
            rel = abs(dim - exp) / exp if exp else 0
            if rel > BBOX_TOLERANCE:
                ok = False
                note_parts.append(f"{name}={dim:.1f} (esperado ~{exp})")
        if not ok:
            note = "Envolvente fuera de tolerancia: " + ", ".join(note_parts)
        else:
            note = f"Envolvente OK: {bbox[0]:.1f} x {bbox[1]:.1f} x {bbox[2]:.1f} mm"

        return {
            "ok": ok,
            "source": source,
            "entities_3d": len(e3),
            "entities_2d": len(e2),
            "bbox_mm": bbox,
            "centroid_match": None,
            "note": note,
        }
    except Exception as exc:
        return {
            "ok": False,
            "source": source,
            "entities_3d": 0,
            "entities_2d": 0,
            "bbox_mm": None,
            "centroid_match": None,
            "note": f"Error gmsh: {exc}",
        }
    finally:
        safe_finally(gmsh.finalize)


def match_centroids(rhino_objs, tolerance=10.0):
    """Match centroide gmsh -> objeto Rhino; retorna conteo de ambiguos."""
    if not HAS_GMSH:
        return None, 0
    gmsh.initialize()
    gmsh.option.setNumber("General.Terminal", 0)
    try:
        gmsh.open(MODEL_STP)
        e3 = gmsh.model.getEntities(3)
        e2 = gmsh.model.getEntities(2)
        entities = e3 + e2
        ambiguous = 0
        matched = 0
        for dim, tag in entities:
            try:
                cg = gmsh.model.occ.getCenterOfMass(dim, tag)
            except Exception:
                continue
            best = None
            best_d = float("inf")
            for o in rhino_objs:
                c = o["centroid"]
                d = math.dist(cg, c)
                if d < best_d:
                    best_d = d
                    best = o
            if best and best_d <= tolerance:
                matched += 1
            else:
                ambiguous += 1
        return {"matched": matched, "ambiguous": ambiguous, "total_entities": len(entities)}, ambiguous
    except Exception as exc:
        return {"error": str(exc)}, 1
    finally:
        safe_finally(gmsh.finalize)


# --------------------------------------------------------------------------- #
# Extraccion de mallas desde rhino3dm
# --------------------------------------------------------------------------- #
def mesh_to_arrays(mesh):
    """Convierte rhino3dm.Mesh a (vertices, faces)."""
    if mesh is None or len(mesh.Vertices) == 0:
        return None, None
    verts = np.array([[v.X, v.Y, v.Z] for v in mesh.Vertices], dtype=float)
    faces = []
    for i in range(len(mesh.Faces)):
        a, b, c, d = mesh.Faces[i]
        if c == d:
            faces.append([a, b, c])
        else:
            faces.append([a, b, c])
            faces.append([a, c, d])
    if not faces:
        return None, None
    return verts, np.array(faces, dtype=int)


def get_mesh_from_geometry(geom):
    """Devuelve (vertices, faces) de una geometria Rhino."""
    t = type(geom).__name__
    if t == "Extrusion":
        return mesh_to_arrays(geom.GetMesh(rhino3dm.MeshType.Any))
    if t == "Brep":
        all_v = []
        all_f = []
        offset = 0
        for face in geom.Faces:
            try:
                v, f = mesh_to_arrays(face.GetMesh(rhino3dm.MeshType.Any))
                if v is None:
                    continue
                all_v.append(v)
                all_f.append(f + offset)
                offset += len(v)
            except Exception:
                continue
        if all_v:
            return np.vstack(all_v), np.vstack(all_f)
    return None, None


# --------------------------------------------------------------------------- #
# Render con matplotlib
# --------------------------------------------------------------------------- #
def render_mesh(verts, faces, output_path, title=None, elev=30, azim=225, dpi=150):
    """Render isometrico sombreado de una malla."""
    if len(faces) == 0:
        raise ValueError("No hay caras para renderizar")
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection="3d")

    polys = verts[faces]
    normals = np.cross(polys[:, 1] - polys[:, 0], polys[:, 2] - polys[:, 0])
    norms = np.linalg.norm(normals, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    normals = normals / norms
    ls = LightSource(azdeg=315, altdeg=45)
    intensity = ls.shade_normals(normals)
    base_color = to_rgba_array("tab:blue")
    facecolors = intensity[:, None] * base_color

    coll = Poly3DCollection(
        polys,
        facecolors=facecolors,
        edgecolors="none",
        alpha=1.0,
    )
    ax.add_collection3d(coll)

    center = verts.mean(axis=0)
    max_span = max(verts.max(axis=0) - verts.min(axis=0))
    margin = max_span * 0.15 if max_span > 0 else 1.0
    ax.set_xlim(verts[:, 0].min() - margin, verts[:, 0].max() + margin)
    ax.set_ylim(verts[:, 1].min() - margin, verts[:, 1].max() + margin)
    ax.set_zlim(verts[:, 2].min() - margin, verts[:, 2].max() + margin)
    ax.set_box_aspect([1, 1, 1])
    ax.view_init(elev=elev, azim=azim)
    ax.set_axis_off()
    if title:
        ax.set_title(title, fontsize=9, pad=0)
    plt.tight_layout()
    fig.savefig(output_path, dpi=dpi, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    if not HAS_GMSH:
        raise SystemExit(
            "ERROR: falta el modulo gmsh. "
            "Crear el entorno e instalar: python3 -m venv .venv-render && "
            ".venv-render/bin/pip install gmsh rhino3dm matplotlib numpy"
        )

    os.makedirs(OUT_DIR, exist_ok=True)

    inventory = load_inventory()
    print(f"Piezas objetivo a renderizar: {len(inventory)}")
    for r in inventory:
        print(f"  - {slugify(r['pieza'])}  ({r['pieza']})")

    print(f"\nLeyendo CAD maestro: {MODEL_3DM}")
    rhino_objs = load_rhino_objects(MODEL_3DM)
    print(f"  Objetos Rhino: {len(rhino_objs)}")

    by_leaf = defaultdict(list)
    for o in rhino_objs:
        by_leaf[o["leaf"]].append(o)

    print("\nDiagnostico gmsh/OCC...")
    diag = gmsh_diagnostic()
    print(f"  Fuente: {diag['source']}")
    print(f"  Entidades 3D: {diag['entities_3d']}, 2D: {diag['entities_2d']}")
    print(f"  Envolvente gmsh: {diag['bbox_mm']}")
    print(f"  {diag['note']}")

    print("\nAlineacion centroide gmsh -> Rhino...")
    match_info, ambiguous = match_centroids(rhino_objs)
    if match_info:
        print(f"  {match_info}")
    if ambiguous > len(rhino_objs) * 0.10:
        print(f"  ADVERTENCIA: {ambiguous} entidades gmsh no alinearon con objetos Rhino")

    # Render individual por pieza
    manifest = []
    complete = True
    print("\nRenderizando piezas individuales...")
    for r in inventory:
        leaf = r["pieza"]
        slug = slugify(leaf)
        objs = by_leaf.get(leaf, [])
        if not objs:
            manifest.append({
                "slug": slug,
                "pieza": leaf,
                "estado": "skipped",
                "triangulos": 0,
                "motivo": "sin objetos en el CAD maestro",
            })
            complete = False
            print(f"  [SKIP] {slug}: sin objetos")
            continue

        all_v = []
        all_f = []
        offset = 0
        for o in objs:
            v, f = get_mesh_from_geometry(o["geom"])
            if v is not None:
                all_v.append(v)
                all_f.append(f + offset)
                offset += len(v)

        if not all_v:
            manifest.append({
                "slug": slug,
                "pieza": leaf,
                "estado": "skipped",
                "triangulos": 0,
                "motivo": "geometria no mallable (VER CAD)",
            })
            complete = False
            print(f"  [SKIP] {slug}: geometria no mallable")
            continue

        verts = np.vstack(all_v)
        faces = np.vstack(all_f)
        out_path = os.path.join(OUT_DIR, f"{slug}.png")
        try:
            render_mesh(verts, faces, out_path, title=leaf)
            manifest.append({
                "slug": slug,
                "pieza": leaf,
                "estado": "rendered",
                "triangulos": int(len(faces)),
                "motivo": "renderizado desde mallas nativas de rhino3dm",
            })
            print(f"  [OK] {slug}: {len(faces)} triangulos")
        except Exception as exc:
            manifest.append({
                "slug": slug,
                "pieza": leaf,
                "estado": "error",
                "triangulos": 0,
                "motivo": f"error matplotlib: {exc}",
            })
            complete = False
            print(f"  [ERROR] {slug}: {exc}")

    # Render del conjunto
    print("\nRenderizando conjunto (_conjunto.png)...")
    all_v = []
    all_f = []
    offset = 0
    target_slugs = {slugify(r["pieza"]) for r in inventory}
    for leaf, objs in by_leaf.items():
        if slugify(leaf) not in target_slugs:
            continue
        for o in objs:
            v, f = get_mesh_from_geometry(o["geom"])
            if v is not None:
                all_v.append(v)
                all_f.append(f + offset)
                offset += len(v)

    if all_v:
        verts = np.vstack(all_v)
        faces = np.vstack(all_f)
        # El conjunto completo puede tener >1M de triangulos; matplotlib no lo
        # renderiza en tiempo razonable. Muestreamos para la vista general.
        MAX_CONJUNTO_TRIANGLES = 120000
        if len(faces) > MAX_CONJUNTO_TRIANGLES:
            rng = np.random.default_rng(seed=42)
            idx = rng.choice(len(faces), size=MAX_CONJUNTO_TRIANGLES, replace=False)
            faces = faces[idx]
        try:
            render_mesh(verts, faces, os.path.join(OUT_DIR, "_conjunto.png"),
                        title="LibreIncu-150 — conjunto de piezas fabricadas",
                        elev=25, azim=230, dpi=150)
            print(f"  [OK] conjunto: {len(faces)} triangulos (muestreados)")
        except Exception as exc:
            print(f"  [ERROR] conjunto: {exc}")
            complete = False
    else:
        print("  [ERROR] conjunto: no se pudieron extraer mallas")
        complete = False

    # Manifiesto
    manifest_data = {
        "aceptacion_completa": complete,
        "gmsh_diagnostico": diag,
        "gmsh_centroid_match": match_info,
        "render_method": "rhino3dm_native_meshes",
        "nota": (
            "El mallado OCC completo del STEP falla con 'overlapping facets'; "
            "las imagenes se generaron a partir de las mallas nativas de rhino3dm "
            "(Extrusion.GetMesh / BrepFace.GetMesh), preservando la identidad por capa."
        ),
        "piezas": manifest,
    }

    with open(os.path.join(OUT_DIR, "manifiesto.json"), "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2, ensure_ascii=False)

    with open(os.path.join(OUT_DIR, "manifiesto.md"), "w", encoding="utf-8") as f:
        f.write("# Manifiesto de renders de piezas\n\n")
        f.write(f"- **aceptacion_completa:** `{complete}`\n")
        f.write(f"- **metodo:** {manifest_data['render_method']}\n")
        f.write(f"- **gmsh:** {diag['note']}\n")
        f.write(f"- **match centroides:** {match_info}\n\n")
        f.write("| Pieza | Slug | Estado | Triangulos | Motivo |\n")
        f.write("|---|---|---|---|---|\n")
        for m in manifest:
            f.write(f"| {m['pieza']} | {m['slug']} | {m['estado']} | {m['triangulos']} | {m['motivo']} |\n")

    print(f"\nManifiesto guardado. aceptacion_completa={complete}")
    return 0 if complete else 1


if __name__ == "__main__":
    sys.exit(main())
