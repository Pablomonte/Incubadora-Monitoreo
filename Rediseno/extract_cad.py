#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extractor de inventario mecanico desde el CAD maestro del rediseno LibreIncu.

Fuente unica: Incubadora-Final.3dm (Rhino, unidades = mm).

Que hace:
  - Agrupa los objetos por CAPA (la capa = la pieza real del diseno).
  - Por cada objeto calcula el bounding box y lo ordena [menor, medio, mayor]
    para distinguir seccion vs largo.
  - Junta instancias identicas -> arma una LISTA DE CORTE / COMPRA real
    (p. ej. "Perfil25-25: 25x25x934 (x1), 30x30x1085 (x2)...").
  - Clasifica cada pieza por uso (estructura/cerramiento/puerta/bandeja/volteo/
    fijacion/comercial/visual) y por nivel de fabricacion.
  - Salidas: cad/inventario.json, cad/inventario.csv, cad/inventario.md.

REGLA CLAVE (sin inventar cotas):
  El bounding box NUNCA se reporta como cota exacta. La confianza es:
    - "estandar"   : pieza comercial cuyo bbox coincide con catalogo (rodamientos, etc.)
    - "envolvente" : medida apta para compra/corte, NO para agujeros/plegados/angulos
    - "instancia"  : bloque/instancia sin geometria explotada -> abrir CAD
  Toda geometria fina se resuelve abriendo el CAD (VER CAD en el manual).
"""

import json
import csv
import os
import collections
import rhino3dm

MODEL = "Incubadora-Final.3dm"
NULL_GUID = "00000000-0000-0000-0000-000000000000"


# --------------------------------------------------------------------------- #
# Capas
# --------------------------------------------------------------------------- #
def build_layer_index(model):
    """Devuelve {layer_index: (ruta_completa, nombre_hoja)}."""
    layers = list(model.Layers)
    by_id = {str(l.Id): l for l in layers}
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


# --------------------------------------------------------------------------- #
# Clasificacion por nombre de capa
# --------------------------------------------------------------------------- #
def categoria(leaf):
    n = leaf.lower()
    if "perfil" in n or "bastidor" in n:
        return "estructura"
    if "chapa" in n or "mdf" in n or "frente" in n:
        return "cerramiento"
    if "door" in n or "puerta" in n or "bisagra" in n or "tapa" in n or "cremay" in n:
        return "puerta"
    if "bandeja" in n or "huevera" in n or "guia" in n or "crema" in n or "hombro" in n:
        return "bandeja"
    if ("polea" in n or "acople" in n or "buje" in n or "rodamiento" in n
            or "correa" in n or "brazo" in n or "avance" in n or "antivib" in n):
        return "volteo"
    if "tornillo" in n or "tuerca" in n or "arandela" in n:
        return "fijacion"
    if "cooler" in n or "bomba" in n or "motor" in n or "ventil" in n:
        return "comercial"
    if "pelo" in n or "letrita" in n or "auxiliar" in n or "regueton" in n:
        return "visual"
    return "otro"


def material(leaf):
    n = leaf.lower()
    if "perfil25" in n:
        return "Tubo estructural 25x25 (la capa tambien incluye perfiles 30x30)"
    if "chapa 1/8" in n:
        return 'Chapa 1/8" (~3.2 mm)'
    if n.startswith("chapa"):
        return "Chapa metalica plegada"
    if "mdf18" in n:
        return "Tablero MDF 18 mm"
    if "mdf55" in n:
        return "Tablero MDF"
    if "ptfe" in n or "buje" in n:
        return "PTFE (mecanizado)"
    if "pa6" in n or ("acople" in n and "8 a 5" not in n):
        return "Nylon PA6 (mecanizado)"
    if "rodamiento626" in n:
        return "Rodamiento 626 - 6x19x6 mm (comercial)"
    if "rodamiento624" in n:
        return "Rodamiento 624 - 4x13x5 mm (comercial)"
    if "hlm8uu" in n:
        return "Rodamiento lineal LM8UU (comercial)"
    if "rodamiento" in n:
        return "Rodamiento (comercial)"
    if "tornillo" in n or "tuerca" in n:
        return "Fijacion comercial"
    if "polea" in n:
        return "Polea dentada"
    if "cooler" in n:
        return "Ventilador / cooler (comercial)"
    if "bomba" in n:
        return "Bomba (comercial)"
    return ""


def fabricacion(cat, leaf):
    n = leaf.lower()
    if cat == "fijacion" or cat == "comercial":
        return "comprar"
    if "rodamiento" in n:
        return "comprar"
    if "perfil" in n:
        return "cortar"
    if "chapa" in n:
        return "cortar + plegar (VER CAD)"
    if "mdf" in n or "frente" in n:
        return "cortar tablero (VER CAD)"
    if "ptfe" in n or "pa6" in n or "buje" in n or "acople" in n or "polea" in n:
        return "mecanizar / imprimir (VER CAD)"
    if cat == "visual":
        return "no fabricable (referencia visual)"
    return "VER CAD"


# --------------------------------------------------------------------------- #
# Geometria
# --------------------------------------------------------------------------- #
def sorted_dims(geom):
    """Bounding box -> [menor, medio, mayor] redondeado a 0.1 mm. None si degenerado."""
    try:
        bb = geom.GetBoundingBox()
    except Exception:
        return None
    d = sorted([round(bb.Max.X - bb.Min.X, 1),
                round(bb.Max.Y - bb.Min.Y, 1),
                round(bb.Max.Z - bb.Min.Z, 1)])
    if d[2] <= 0:
        return None
    return d


def is_block_instance(geom, dims):
    """Heuristica: instancia de bloque sin explotar -> bbox degenerado (<1mm en 2 ejes)."""
    if dims is None:
        return True
    return dims[0] < 1.0 and dims[1] < 1.0


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)
    if not os.path.exists(MODEL):
        raise SystemExit(f"No se encontro {MODEL} en {here}")

    model = rhino3dm.File3dm.Read(MODEL)
    layer_idx = build_layer_index(model)

    # Acumuladores por pieza (capa hoja)
    pieces = collections.OrderedDict()
    overall_min = [1e18, 1e18, 1e18]
    overall_max = [-1e18, -1e18, -1e18]

    for obj in model.Objects:
        attr = obj.Attributes
        geom = obj.Geometry
        path, leaf = layer_idx.get(attr.LayerIndex, ("?", "?"))

        try:
            bb = geom.GetBoundingBox()
            for k, (mn, mx) in enumerate([(bb.Min.X, bb.Max.X),
                                          (bb.Min.Y, bb.Max.Y),
                                          (bb.Min.Z, bb.Max.Z)]):
                overall_min[k] = min(overall_min[k], mn)
                overall_max[k] = max(overall_max[k], mx)
        except Exception:
            pass

        dims = sorted_dims(geom)
        key = leaf
        if key not in pieces:
            pieces[key] = {
                "pieza": leaf,
                "ruta_cad": path,
                "cantidad": 0,
                "tamanos": collections.Counter(),   # signature -> count
                "bloques": 0,
                "categoria": categoria(leaf),
                "material": material(leaf),
            }
        p = pieces[key]
        p["cantidad"] += 1
        if is_block_instance(geom, dims):
            p["bloques"] += 1
        else:
            sig = "x".join(f"{v:.0f}" for v in dims)  # "25x25x934"
            p["tamanos"][sig] += 1

    overall = [round(overall_max[k] - overall_min[k], 1) for k in range(3)]

    # Construir inventario final
    inventory = []
    for p in pieces.values():
        cat = p["categoria"]
        fab = fabricacion(cat, p["pieza"])
        # confianza
        if "comprar" in fab and ("rodamiento" in p["pieza"].lower()
                                 or "tornillo" in p["pieza"].lower()
                                 or "tuerca" in p["pieza"].lower()):
            conf = "estandar"
        elif p["bloques"] and not p["tamanos"]:
            conf = "instancia (VER CAD)"
        else:
            conf = "envolvente"

        # lista de tamanos legible, ordenada por largo desc
        sizes = sorted(p["tamanos"].items(),
                       key=lambda kv: float(kv[0].split("x")[-1]), reverse=True)
        sizes_str = "; ".join(f"{sig} (x{n})" for sig, n in sizes)
        if p["bloques"]:
            extra = f"{p['bloques']} bloque(s) sin explotar"
            sizes_str = (sizes_str + "; " + extra) if sizes_str else extra

        inventory.append({
            "pieza": p["pieza"],
            "ruta_cad": p["ruta_cad"],
            "cantidad": p["cantidad"],
            "tamanos_mm": sizes_str,
            "tamanos_detalle": dict(p["tamanos"]),
            "categoria": cat,
            "material": p["material"],
            "fabricacion": fab,
            "confianza": conf,
        })

    # Orden: por categoria (segun prioridad) y luego por cantidad desc
    orden_cat = ["estructura", "cerramiento", "puerta", "bandeja", "volteo",
                 "fijacion", "comercial", "otro", "visual"]
    inventory.sort(key=lambda r: (orden_cat.index(r["categoria"])
                                  if r["categoria"] in orden_cat else 99,
                                  -r["cantidad"]))

    os.makedirs("cad", exist_ok=True)

    meta = {
        "modelo": MODEL,
        "unidades": "mm",
        "envolvente_total_mm": overall,
        "nota": ("Dimensiones = bounding box (envolvente). No son cotas de "
                 "agujeros/plegados/angulos: para geometria fina abrir el CAD."),
    }

    with open("cad/inventario.json", "w", encoding="utf-8") as f:
        json.dump({"meta": meta, "piezas": inventory}, f, indent=2, ensure_ascii=False)

    cols = ["Pieza", "Ruta CAD", "Cantidad", "Tamanos envolventes mm (sig x N)",
            "Material/nota", "Categoria", "Fabricacion", "Confianza"]
    with open("cad/inventario.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in inventory:
            w.writerow([r["pieza"], r["ruta_cad"], r["cantidad"], r["tamanos_mm"],
                        r["material"], r["categoria"], r["fabricacion"], r["confianza"]])

    with open("cad/inventario.md", "w", encoding="utf-8") as f:
        f.write("# Inventario mecanico extraido del CAD maestro\n\n")
        f.write(f"- **Modelo:** `{MODEL}` (Rhino, unidades **mm**)\n")
        f.write(f"- **Envolvente total:** {overall[0]} x {overall[1]} x {overall[2]} mm "
                "(ancho x prof x alto aprox.)\n")
        f.write("- **Tamanos = bounding box (envolvente).** No son cotas de "
                "agujeros, plegados ni angulos: para geometria fina **abrir el CAD**.\n")
        f.write("- Notacion de tamanos: `seccion_menor x seccion_media x largo (xN)`, "
                "una entrada por cada medida distinta dentro de la pieza.\n\n")
        last = None
        for r in inventory:
            if r["categoria"] != last:
                last = r["categoria"]
                f.write(f"\n## {last.capitalize()}\n\n")
                f.write("| Pieza | Ruta CAD | Cant | Tamanos envolventes mm | "
                        "Material / nota | Fabricacion | Confianza |\n")
                f.write("|---|---|---|---|---|---|---|\n")
            f.write(f"| {r['pieza']} | {r['ruta_cad']} | {r['cantidad']} | "
                    f"{r['tamanos_mm']} | {r['material']} | {r['fabricacion']} | "
                    f"{r['confianza']} |\n")

    print(f"OK - {len(inventory)} piezas. Envolvente {overall} mm. "
          "Salidas en cad/inventario.{json,csv,md}")


if __name__ == "__main__":
    main()
