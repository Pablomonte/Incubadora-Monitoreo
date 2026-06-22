# Compra y corte

Esta pagina resume que comprar, que cortar y que fabricar. El inventario completo de 162 tipos queda en la pagina Inventario CAD.

## Ficha rapida de compra

| Grupo | Comprar |
|---|---|
| Rodamientos | 626 x11, 624 x3, HLM8UU x1. |
| Tornilleria | M3, M4, M5 y tuercas M3/M4/M5/M6/M8 segun Inventario CAD. |
| Actuadores | Bomba 12 V, cooler, motorreductor 12 V para volteo. |
| Potencia | Fuente 12 V 5 A, LM2596, resistencia 200 W, ventilador/turbina 220 VAC. |
| Control | Placa Olivia v0.2, ESP32-WROOM-32D, BME280, reeds de final de carrera. |
| Seguridad electrica | Disyuntor, termomagneticas, gabinete IP65, riel DIN, prensacables, puesta a tierra. |

## Ficha rapida de corte mecanico

| Material | Preparacion |
|---|---|
| Tubo estructural | Cortar perfiles 25x25, 30x30 y 40x40 segun mini-BOM de cajon. |
| Chapas | Cortar y plegar con CAD abierto. No usar solo bounding box. |
| MDF | Cortar paneles; verificar espesor real y escuadra. |
| Policarbonato | Cortar frente; proteger caras hasta el montaje final. |
| Piezas impresas/mecanizadas | Preparar acoples, guias, bujes y piezas del giro con CAD abierto. |

## Resumen generado por componente

--8<-- "cad/resumen_componentes.md"

## Criterios de recepcion

- Las piezas comerciales deben coincidir con su medida nominal o catalogo.
- Los perfiles cortados deben tener rebabas removidas y extremos escuadrados.
- Chapas y tableros deben presentarse en seco antes de fijar definitivamente.
- Las piezas marcadas `VER CAD` no pasan a fabricacion sin revisar modelo y orientacion.

## Separar por bandejas de taller

Preparar cajas o bandejas fisicas con estas etiquetas:

- Cajon y estructura.
- Contrafondo y cerramientos.
- Mecanismo de giro.
- Transmision y guiado.
- Bandejas y bastidor giratorio.
- Puerta.
- Actuadores y electrica.
- Tornilleria.
