# Antes de fabricar

Esta pagina fija el alcance, las convenciones y las condiciones minimas para trabajar con el manual sin confundir inventario CAD con plano de taller.

## Alcance

El manual sirve para:

- Preparar compra y corte.
- Fabricar o imprimir piezas segun el CAD.
- Montar subconjuntos mecanicos.
- Cablear y probar actuadores, sensores y placa Olivia.
- Ejecutar una puesta en marcha sin huevos.

No es un plano de mecanizado completo. Cuando una pieza requiere agujeros, plegados, alojamientos, tolerancias o posicion exacta, el procedimiento indica `VER CAD`.

## Convenciones

| Marca | Uso |
|---|---|
| `OK FABRICAR` | Hay informacion suficiente para comprar, cortar o preparar. |
| `OK MONTAR` | El subconjunto puede montarse siguiendo este manual y verificaciones simples. |
| `VER CAD` | Hace falta abrir el modelo maestro para geometria fina. |
| `estandar` | Pieza comercial reconocible por catalogo o medida normalizada. |
| `envolvente` | Medida de bounding box apta para compra/corte general. |
| `instancia` | Bloque o instancia que debe verificarse en CAD. |

!!! info "Fuente de las medidas"
    El inventario se genera desde `Rediseno/Incubadora-Final.3dm`. Las tablas usan milimetros y nombres funcionales; la capa CAD aparece como referencia secundaria.

## Herramientas recomendadas

| Area | Herramientas |
|---|---|
| Medicion | Cinta metrica, calibre, escuadra, nivel, marcador fino. |
| Corte y preparacion | Sierra o sensitiva para perfiles, herramientas para chapa, taladro, mechas, lima, desbarbador. |
| Montaje mecanico | Llaves Allen, llaves fijas, destornilladores, prensas, sargentos. |
| Electrica | Multimetro, pinza amperometrica si hay, crimpeadora, terminales, borneras, termocontraible. |
| Seguridad | Guantes, gafas, proteccion auditiva, disyuntor diferencial, puesta a tierra verificada. |

## Antes de cortar

- [ ] Confirmar que el CAD maestro disponible corresponde a LibreIncu-150.
- [ ] Leer completa la pagina de compra y corte.
- [ ] Separar piezas en `comprar`, `cortar`, `fabricar / imprimir` y `VER CAD`.
- [ ] Revisar que las chapas y tableros tengan margen para ajustes de taller.
- [ ] Definir quien valida las partes electricas de 220 VAC.

## Riesgos principales

!!! danger "Electricidad y humedad"
    La incubadora combina 220 VAC, calefaccion, ventilacion, agua y humedad. No energizar con tapas abiertas, cables sueltos, tierra dudosa o separacion AC/DC deficiente.

!!! warning "Geometria fina"
    No perforar ni plegar solo con las dimensiones de inventario. Para posiciones de agujeros, plegados, alojamientos de rodamientos, ejes y cremallera, abrir el CAD.

!!! warning "Alineacion mecanica"
    El mecanismo de giro necesita ejes paralelos, acoples libres y bandejas sin roce. Una pieza ligeramente desalineada puede trabar el volteo.
