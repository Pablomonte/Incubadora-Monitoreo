# Instalacion electrica

!!! danger "220 VAC"
    La instalacion trabaja con tension de red, calefactor, ventilacion, agua y humedad. Debe montarla o revisarla una persona competente. No energizar sin puesta a tierra, disyuntor diferencial, separacion AC/DC, prensacables y gabinete cerrado.

## Checklist electrica segura

- [ ] Gabinete electrico IP65 con riel DIN.
- [ ] Entrada 220 VAC protegida por disyuntor diferencial bipolar.
- [ ] Termomagneticas separadas para electronica, calefactor y cargas auxiliares.
- [ ] Puesta a tierra continua en gabinete y partes metalicas.
- [ ] Separacion fisica entre AC y DC.
- [ ] Prensacables y alivio de traccion.
- [ ] Primer encendido sin cargas conectadas.
- [ ] Medicion de 12 V y ajuste de LM2596 a 5 V antes de conectar ESP32.

## Potencia y actuadores

| Sistema | Elementos |
|---|---|
| Alimentacion | Fuente switching 12 V 5 A, step-down LM2596 a 5 V. |
| Calefaccion | Resistencia 200 W comandada por TRIAC. |
| Ventilacion | Ventilador/turbina 220 VAC y cooler segun montaje. |
| Humidificacion | Bomba 12 V comandada por salida de potencia. |
| Rotación | Motorreductor 12 V mediante puente H L298. |
| Sensado | BME280 por I2C y dos reed switches como finales de carrera. |

## Placa Olivia v0.2

- MCU: ESP32-WROOM-32D.
- Potencia AC: TRIAC BTA16-800B, MOC3041SM y TLP181 para cruce por cero.
- Alimentacion on-board: modulo HW-613.
- Conectores: Molex SL, Phoenix GMSTB y headers de programacion.

## Mapa de señales ESP32

| GPIO | Señal | Destino |
|---:|---|---|
| 2 | VOLTEO_UP / IN_A_N | L298 IN1 |
| 15 | VOLTEO_DOWN / IN_A_P | L298 IN2 |
| 13 | VOLTEO_EN / EN_A | L298 ENA |
| 14 | RESISTOR | TRIAC resistencia 200 W |
| 17 | HUMID | Bomba / humidificacion |
| 35 | REED_UP | Reed superior |
| 34 | REED_DOWN | Reed inferior |
| 32 | SDA | BME280 I2C |
| 33 | SCL | BME280 I2C |

## Prueba sin cargas

1. Verificar continuidad de tierra.
2. Medir que no haya corto entre linea, neutro y tierra.
3. Energizar solo fuente.
4. Medir 12 V.
5. Ajustar LM2596 a 5 V.
6. Conectar placa Olivia.
7. Validar lectura del BME280.
8. Conectar cargas de a una.

!!! warning "Agua y cables"
    La bomba y el circuito de agua deben quedar por debajo o aislados de borneras y placa. Usar goteo dirigido, prensacables y recorrido de cables que no conduzca agua hacia la electronica.
