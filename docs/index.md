# LibreIncu-150

Manual de fabricacion, montaje y puesta en marcha del rediseno LibreIncu-150.

LibreIncu es una incubadora de huevos pensada como tecnologia abierta para la Agricultura Familiar, Campesina e Indigena. El objetivo es que una comunidad, taller o fabrica local pueda construir, reparar y adaptar la maquina sin depender de una caja cerrada.

Esta version documenta el rediseño mecanico LibreIncu-150: gabinete, bandejas, mecanismo de giro, actuadores, instalacion electrica, placa Olivia v0.2 y puesta en marcha.

[Descargar manual PDF](manual_libreincu_150.pdf){ .md-button .md-button--primary }
[Ver inventario CAD](inventario.md){ .md-button }
[Ver modelo 3D](vista-3d.md){ .md-button }

![Conjunto LibreIncu-150](img/piezas/_conjunto.png){ width=680 }

## Que se puede hacer con este manual

- Comprar piezas comerciales, perfiles, placas, chapas, actuadores y fijaciones.
- Cortar y preparar piezas usando medidas de envolvente extraidas del CAD.
- Montar los subconjuntos mecanicos principales con apoyo visual.
- Cablear la instalacion electrica con controles de seguridad.
- Poner en marcha la incubadora y diagnosticar fallas frecuentes.

!!! warning "Que no reemplaza este manual"
    Las medidas mecanicas provienen del bounding box de cada pieza. Sirven para compra, corte y control general. Agujeros, plegados, angulos, tolerancias, alojamientos y posiciones finas se resuelven abriendo el CAD maestro cuando el manual indica `VER CAD`.

## Como leer este manual

1. **Antes de fabricar**: alcance, herramientas, criterios de seguridad y convenciones.
2. **Compra y corte**: listas resumidas para preparar materiales sin leer el inventario completo.
3. **Montaje mecanico**: una seccion por componente, con locator, vista del subconjunto, mini-BOM y controles.
4. **Instalacion electrica**: potencia, placa Olivia, GPIO y seguridad de 220 VAC.
5. **Puesta en marcha**: checklist de prueba sin huevos y validacion por etapas.
6. **Troubleshooting**: diagnostico guiado por sintoma.
7. **Inventario CAD**: referencia tecnica completa generada desde el modelo.

## De un vistazo

| Sistema | Resumen |
|---|---|
| Estructura | Bastidor de tubos 25x25, 30x30 y una pieza 40x40 mm. |
| Cerramiento | Chapas metalicas, MDF 18 mm y frente de policarbonato. |
| Temperatura | Resistencia calefactora 200 W, ventilacion y lectura BME280. |
| Humidificacion | Bomba 12 V y circuito de agua controlado por la placa. |
| Rotacion | Mecanismo de giro con ejes, acoples, rodamientos, polea y cremallera. |
| Control | Placa Olivia v0.2 con ESP32-WROOM-32D. |
| Conectividad | WiFi para operacion local y monitoreo del sistema. |

## Dimensiones de referencia

- **Envolvente cuerpo:** 604.8 x 1233.5 x 1170.4 mm.
- **Envolvente total CAD:** 604.8 x 1263.9 x 1189.2 mm.
- **Unidades:** milimetros.

La envolvente total incluye elementos en posicion abierta o de referencia. Para fabricar o ubicar piezas, seguir siempre las notas de cada componente y el CAD.
