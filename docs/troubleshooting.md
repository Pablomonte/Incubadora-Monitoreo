# Troubleshooting

Diagnostico guiado para fallas frecuentes. Trabajar sin tension antes de tocar cableado o mecanica.

| Sintoma | Prueba | Causa probable | Accion |
|---|---|---|---|
| No enciende | Medir entrada 220 VAC y salida de fuente | Disyuntor, termomagnetica, fusible o fuente | Revisar protecciones, continuidad y fuente antes de conectar placa. |
| Placa no arranca | Medir 5 V en Olivia | LM2596 mal ajustado o cableado DC | Ajustar a 5 V y revisar polaridad. |
| No mide temperatura/humedad | Escanear I2C o medir GPIO32/33 | BME280 sin alimentacion, direccion o cableado incorrecto | Revisar VCC/GND/SDA/SCL y direccion del sensor. |
| No calienta | Medir GPIO14 y salida del TRIAC | TRIAC, opto o resistencia desconectada | Probar comando, continuidad de resistencia y etapa de potencia. |
| Calienta de mas | Verificar lectura BME280 y control | Sensor mal ubicado o salida trabada | Cortar energia, revisar sensor y TRIAC. |
| No ventila | Activar salida y medir carga | Ventilador sin alimentacion o cableado suelto | Revisar borneras, fusible y comando. |
| No humidifica | Activar bomba y revisar nivel | Bomba descebada, manguera obstruida o salida fallando | Cebar, limpiar circuito y medir salida. |
| Pierde agua | Inspeccion visual con bomba corta | Manguera, union o boquilla floja | Ajustar abrazaderas y alejar agua de electronica. |
| No gira | Activar L298 y medir motor | Puente H, motorreductor o atasco mecanico | Desacoplar motor y probar giro manual. |
| Gira al reves | Activar subida/bajada y observar | Motor invertido o logica cruzada | Invertir cables del motor o corregir IN_A_N/IN_A_P. |
| No detecta reed | Medir continuidad con iman | Reed mal ubicado o sin pull-up | Ajustar posicion del iman y revisar GPIO34/35. |
| Se traba el volteo | Girar manualmente sin motor | Cremallera, polea, eje o bandeja desalineados | Reabrir CAD, alinear guias y liberar roces. |
| Cierre de puerta deficiente | Prueba de luz o papel | Bisagra, frente o burlete mal asentado | Ajustar bisagras y verificar frente de policarbonato. |

## Orden de diagnostico recomendado

1. Separar mecanica de electrica: probar giro a mano antes de culpar al motor.
2. Probar alimentacion antes de revisar firmware.
3. Probar sensores antes de automaticos.
4. Probar cargas una por una.
5. Registrar que cambio produjo la falla.

!!! danger "No puentear protecciones"
    No anular disyuntor, tierra, termomagneticas ni finales de carrera para "probar rapido". Si una proteccion actua, encontrar la causa.
