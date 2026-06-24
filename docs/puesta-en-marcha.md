# Puesta en marcha

La puesta en marcha se hace sin huevos y por etapas. No probar automaticos antes de comprobar cada salida manualmente.

## Checklist en 15 pasos

1. Inspeccionar tornilleria, bordes y holguras con la incubadora sin tension.
2. Rotar manualmente el mecanismo de bandejas.
3. Confirmar que no haya roce con puerta, chapas o cerramientos.
4. Revisar continuidad de tierra.
5. Verificar separacion AC/DC y gabinete cerrado.
6. Encender fuente sin cargas.
7. Medir 12 V.
8. Ajustar LM2596 a 5 V.
9. Encender placa Olivia.
10. Confirmar lectura coherente del BME280.
11. Probar calefactor por activacion corta.
12. Probar ventilacion.
13. Probar bomba con agua controlada y sin salpicaduras.
14. Probar rotación manual, sentido de giro y detencion por reeds.
15. Ejecutar ciclo sin huevos hasta estabilizar temperatura, humedad y una rotación completa.

## Valores a registrar

| Prueba | Registrar |
|---|---|
| Alimentacion | 12 V y 5 V medidos. |
| Sensor | Temperatura y humedad ambiente al encender. |
| Calefaccion | Tiempo hasta primera subida de temperatura. |
| Humidificacion | Tiempo de bomba, nivel de agua y ausencia de fugas. |
| Rotación | Sentido, tiempo de carrera, reed superior e inferior. |
| Red | Nombre de red WiFi y acceso a interfaz / monitoreo. |

## Criterio de aceptacion

- La incubadora puede permanecer encendida sin olor, calentamiento anormal de cables ni disparos de proteccion.
- El sensor lee valores estables y razonables.
- La resistencia, ventilacion, bomba y motor responden por separado.
- El mecanismo de rotación completa el recorrido y se detiene por finales de carrera.
- No hay agua cerca de borneras, fuente o placa.

!!! tip "Primera corrida"
    Dejar al menos un ciclo completo sin huevos antes de uso productivo. Registrar fallas, ruidos y tiempos; corregir mecanica antes de ajustar software.
