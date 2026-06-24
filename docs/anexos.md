# Anexos y archivos fuente

## Archivos principales

| Archivo | Uso |
|---|---|
| `Rediseno/Incubadora-Final.3dm` | CAD maestro Rhino. |
| `Rediseno/extract_cad.py` | Genera inventario y mini-BOMs desde CAD. |
| `Rediseno/render_parts.py` | Genera renders de piezas, subconjuntos y locators. |
| `Rediseno/cad/inventario.json` | Fuente estructurada del inventario. |
| `Rediseno/cad/inventario.md` | Inventario completo para MkDocs. |
| `Rediseno/cad/resumen_componentes.md` | Mini-BOM por componente para el flujo principal. |
| `docs/img/componentes/` | Locators y subconjuntos por componente. |
| `docs/img/piezas/` | Renders individuales y conjunto. |

## Galeria de piezas

Vista isometrica del conjunto:

![Conjunto LibreIncu-150](img/piezas/_conjunto.png){ width=640 }

### Piezas mecanicas representativas

| | |
|---|---|
| ![Perfil estructural](img/piezas/perfil25-25.png){ width=320 } | ![Chapa caja](img/piezas/chapa-caja.png){ width=320 } |
| ![MDF 18 mm](img/piezas/mdf18mm.png){ width=320 } | ![Frente policarbonato](img/piezas/frente-pc.png){ width=320 } |
| ![Polea dentada](img/piezas/poleadentada.png){ width=320 } | ![Cremallera dentada](img/piezas/cremayera.png){ width=320 } |
| ![Acople bandeja-eje](img/piezas/acoplebandejaeje.png){ width=320 } | ![Bandeja huevera](img/piezas/huevera.png){ width=320 } |

## Reproducir documentacion tecnica

```bash
python3 Rediseno/extract_cad.py
.venv-render/bin/python Rediseno/render_parts.py
mkdocs build --strict
```

El render usa mallas nativas de `rhino3dm`.
