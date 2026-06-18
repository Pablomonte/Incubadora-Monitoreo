# Plan Operativo — Guía de montaje e inventario del rediseño LibreIncu (rama LibreIncu-150)

## 1. Alcance
Este documento no promete ser un plano de taller completo para cada pieza. Funciona como:
- Inventario mecánico trazable al CAD maestro.
- Guía de montaje paso a paso.
- Base de compra, corte, preparación y verificación.
- Referencia eléctrica y de puesta en marcha.

**Nota:** Cuando falten agujeros, plegados, ángulos, tolerancias o mecanizados críticos, se marca **VER CAD** en las instrucciones.

## 2. Fuentes del documento
- **Mecánica:** `Rediseno/Incubadora-Final.3dm` (única fuente válida).
- **Electrónica general:** `HardWare/Electro/NOMENCLATURA_LibreIncu.md`, `EsquemaLibreIncu.qet`, `libreincu_BOM.csv`.
- **Placa Olivia:** `HardWare/Electro/Olivia_control/v0.2/`.
- **Puesta en marcha:** `src/embedded/README.md` y comportamiento observable del firmware.

**Archivos descartados para mecánica del rediseño:**
- `ALT-INC001-*`
- `SistemaBasculantePlanos.pdf`

La discrepancia eléctrica ha sido verificada y el esquema es correcto.

## 3. Convenciones
- **OK FABRICAR:** Datos suficientes en este documento para compra, corte o preparación.
- **OK MONTAR:** Pieza lista para ensamblar en el equipo.
- **VER CAD:** Requiere la geometría fina del modelo maestro para una correcta fabricación.

## 4. BOM consolidada

### Mecánica (desde CAD)
| Pieza | Ruta CAD | Cantidad | Dimensiones envolventes mm | Material/nota | Uso | Nivel de fabricacion | Confianza | Accion |
|---|---|---|---|---|---|---|---|---|
| Pieza | Ruta CAD | Cantidad | Dimensiones envolventes mm | Material/nota | Uso | Nivel de fabricacion | Confianza | Accion |
|---|---|---|---|---|---|---|---|---|
| S�lido importado1 | BombaStuff | 6 | 168.0x240.4x207.6 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado1 | BASE | 43 | 588.0x330.0x1170.4 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| PLANAR_3 | BASE | 1 | 6.6x67.2x28.7 | Desconocido | otro | imprimir | envolvente | Imprimir |
| CYL_28 | BASE | 1 | 12.0x18.1x38.4 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| PLANAR_15 | BASE | 1 | 27.6x95.0x6.6 | Desconocido | otro | imprimir | envolvente | Imprimir |
| CYL_29 | BASE | 1 | 19.2x44.4x38.4 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado1 | Chapa-Caja | 1 | 458.6x333.1x85.2 | Desconocido | cerramiento | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado1 | BoquillaAltaP | 5 | 43.9x50.4x20.4 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado1 | Chapa-Paredon | 2 | 379.2x359.0x290.8 | Desconocido | cerramiento | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado2 | Chapa-SoporteInferior | 1 | 24.0x504.0x24.0 | Desconocido | cerramiento | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado3 | Chapa-SoporteInferior | 1 | 24.0x504.0x24.0 | Desconocido | cerramiento | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado1 | Chapa-SoporteInferior | 2 | 486.0x192.0x24.0 | Desconocido | cerramiento | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado1 | Reguetones | 14 | 48.0x48.0x39.5 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado2 | BombaStuff | 2 | 67.2x107.3x107.3 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado3 | BombaStuff | 2 | 37.2x107.3x107.3 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | Bandeja::huevera | 23 | 0.1x0.1x0.2 | Desconocido | bandeja | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | Rodamiento626 | 11 | 6.0x19.0x19.0 | comercial | otro | comercial (comprar) | envolvente | Comprar |
| S�lido importado1 | AcopleBandejaEje | 75 | 55.2x18.8x18.8 | Desconocido | bandeja | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | TuercasM6 | 82 | 11.1x14.0x14.0 | Desconocido | fijacion | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | Tuercas M3 | 11 | 9.0x9.0x9.0 | fijación comercial | fijacion | comercial (comprar) | envolvente | Comprar |
| Unnamed | Tornillo M3 | 27 | 16.0x24.8x11.6 | fijación comercial | fijacion | comercial (comprar) | envolvente | Comprar |
| S�lido importado5 | BASE | 1 | 48.0x18.0x60.0 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado8 | BASE | 2 | 45.3x53.8x40.6 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado10 | BASE | 1 | 24.9x24.0x24.0 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado13 | BASE | 1 | 95.8x48.0x21.6 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado2 | BASE | 1 | 132.0x48.0x96.0 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado7 | BASE | 1 | 108.0x48.0x40.7 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado3 | BASE | 1 | 24.0x18.0x48.0 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado11 | BASE | 1 | 95.8x48.0x21.6 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado9 | BASE | 1 | 372.0x108.0x252.0 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado6 | BASE | 1 | 48.0x18.0x48.0 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado4 | BASE | 1 | 120.0x18.0x108.0 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado12 | BASE | 1 | 95.8x48.0x21.6 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | Tuercas M4 | 5 | 3.2x11.5x11.5 | fijación comercial | fijacion | comercial (comprar) | envolvente | Comprar |
| Unnamed | Auxiliar1 | 29 | 22.6x487.9x147.9 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | BandejasFijas | 12 | 98.4x480.6x18.0 | Desconocido | bandeja | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | ACOPLE 8 a 5 | 17 | 30.5x15.3x310.0 | Desconocido | volteo | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | Barra Avance Z | 2 | 30.5x8.2x8.2 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | Tuercas M8 | 2 | 7.4x15.6x15.6 | Desconocido | fijacion | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | HerrajesTraseros | 3 | 113.5x37.5x136.0 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | Letritas | 10 | 0.2x21.5x20.2 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | ChapaCooler | 3 | 461.3x232.0x169.7 | Desconocido | cerramiento | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | Buje-PTFE | 2 | 3.7x5.3x311.0 | PTFE | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | Pelos | 780 | 18.8x0.2x0.2 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | Tapas | 4 | 386.6x10.8x277.1 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| CYL_10 | Auxiliar1 | 1 | 28.8x19.0x38.4 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado1 | Auxiliar1 | 2 | 13.3x15.9x13.3 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | VentilacionDoor | 2 | 30.9x22.1x22.1 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | MDF18mm | 4 | 601.4x784.2x1169.0 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | HombroBandej | 6 | 13.8x32.8x89.2 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | Tornillo M4 | 18 | 29.7x7.4x7.4 | fijación comercial | fijacion | comercial (comprar) | envolvente | Comprar |
| Unnamed | Rodamiento624 | 3 | 5.0x13.0x13.0 | comercial | otro | comercial (comprar) | envolvente | Comprar |
| Unnamed | AcoplesPA6 | 3 | 6.3x26.8x30.7 | PA6 | volteo | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | Chapa 1/8 | 8 | 121.6x92.3x260.9 | chapa 1/8" | cerramiento | cortar | envolvente | Cortar |
| S�lido importado1 | BandejasFijas | 3 | 480.0x18.0x18.0 | Desconocido | bandeja | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | FondoBrazo | 2 | 6.0x40.3x329.4 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | U 2219 - Door | 4 | 26.4x541.9x1014.6 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | FRENTE-PC | 2 | 4.8x486.2x1189.2 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado1 | BisagraP | 4 | 34.9x34.9x75.6 | Desconocido | puerta | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado1 | Cooler | 1 | 204.0x173.9x153.5 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | Perfil25-25 | 20 | 576.9x653.5x1085.5 | tubo 25x25 | estructura | cortar | envolvente | Cortar |
| Unnamed | MDF55 | 2 | 497.2x6.6x1021.1 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | RodamientoHLM8UU | 1 | 18.9x18.9x53.8 | comercial | otro | comercial (comprar) | envolvente | Comprar |
| Unnamed | Tuercas M5 | 8 | 12.3x12.3x12.3 | fijación comercial | fijacion | comercial (comprar) | envolvente | Comprar |
| Unnamed | Tornillo M5 | 24 | 25.9x48.0x10.0 | fijación comercial | fijacion | comercial (comprar) | envolvente | Comprar |
| S�lido importado1 | PoleaDentada | 1 | 33.1x50.2x50.2 | Desconocido | volteo | ver_CAD | exacta | Ver_cad con CAD abierto |
| S�lido importado1 | Auxiliar2 | 1 | 121.1x43.2x43.2 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | Auxiliar3 | 1 | 73.2x28.6x70.9 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | SoporT-AntiVib | 1 | 72.6x28.6x63.8 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | SeparadorPAI | 1 | 4.0x75.2x89.5 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | Cremayera | 4 | 23.5x64.6x212.8 | Desconocido | otro | ver_CAD | exacta | Ver_cad con CAD abierto |
| Unnamed | GUIA-CREMA | 3 | 20.7x62.7x316.6 | Desconocido | bandeja | ver_CAD | exacta | Ver_cad con CAD abierto |


### Actuadores, sensores y alimentación (desde libreincu_BOM.csv)
- **Fuente switching:** 12V 5A con ventilación.
- **Módulo step down:** LM2596 regulable (ajustar a 5V).
- **Resistencia calefactora:** 200W (tipo panchera industrial).
- **Ventilador turbina:** 220 VAC 50Hz, 120x120mm axial con rulemán.
- **Bomba de agua:** 12VCC 4.3 LPM 35 PSI.
- **Sensor:** BME280 (Temperatura / humedad / presión I²C).
- **Sensores Reed:** Magnéticos para puerta/volteo x2.
- **Protecciones:** Disyuntor bipolar 2x 25A, termomagnéticas Q1–Q4, llaves on/off.

### Placa Olivia (desde bill-of-materials-UPDATED.csv)
- **Microcontrolador:** ESP32-WROOM-32D (U1)
- **Aislación y conmutación:** MOC3041SM (Opto TRIAC), TLP181 (Opto), BTA16-800B (TRIAC x2).
- **Entradas/Salidas:** Conectores Molex SL, Phoenix GMSTB, Jumper headers.
- **Alimentación integrada:** HW-613 (DC-DC).

## 5. Preparación de piezas
1. **Comerciales:** Comprar según la BOM consolidada y lista de inventario.
2. **Perfiles y cortes:** Cortar perfiles de bastidor según longitud del inventario mecánico.
3. **Chapas y cerramientos:** Cortar. Para plegar (**VER CAD**).
4. **Bandejas y guías:** Cortar o comprar según especificaciones envolventes.
5. **Sistema de volteo:** Cortar ejes, mecanizar acoples (**VER CAD**), preparar motorreductor.
6. **Fijaciones:** Seleccionar tornillería adecuada.
7. **Impresión 3D:** Imprimir componentes clasificados como "imprimir".

## 6. Montaje mecánico
1. **Bastidor Perfil25-25**
   - *Piezas:* Perfiles tubulares 25x25.
   - *Acción:* Ensamblar estructura base.
   - *Riesgo:* Descuadre.
   - *Resultado:* Marco rígido y escuadrado.
2. **Gabinete y chapas**
   - *Piezas:* Chapas de cerramiento, aislación.
   - *Acción:* Fijar chapas al bastidor.
   - *Riesgo:* Fugas de aire.
   - *Resultado:* Gabinete cerrado térmicamente.
3. **Puertas/tapas/bisagras**
   - *Piezas:* Puerta principal, bisagras.
   - *Acción:* Montar y alinear la puerta.
   - *Control:* Cierre hermético.
   - *Resultado:* Apertura y cierre suave.
4. **Bandejas fijas y móviles**
   - *Piezas:* Bandejas, malla.
   - *Acción:* Ubicar en posición.
   - *Resultado:* Soporte para los huevos.
5. **Guías y cremalleras**
   - *Piezas:* Guías laterales.
   - *Acción:* Fijar al bastidor/chapas.
   - *Resultado:* Deslizamiento correcto.
6. **Sistema de volteo**
   - *Piezas:* Motorreductor, correas, poleas, eje.
   - *Acción:* Instalar motor y acoplar a las bandejas.
   - *Control:* Tensión de correa y alineación.
   - *Resultado:* Movimiento suave del mecanismo.
7. **Alineación final**
   - *Acción:* Repaso general de tornillos y holguras.

## 7. Sistema de volteo (detalle)
- **Componentes:** Motorreductor 12 V 17 rpm, eje, rodamientos (624/626/HLM8UU), buje PTFE, polea dentada, correa, acoples PA6, acople bandeja-eje, reeds sup/inf (finales de carrera).
- **Importante:** Se debe marcar **VER CAD** para toda posición de eje, agujero de soporte y tensión de correa que no salga de forma inequívoca del inventario.

## 8. Instalación eléctrica
- **Componentes:** Gabinete eléctrico, entrada 220 VAC, disyuntor + termomagnéticas Q1–Q4.
- **Fuentes:** Fuente 12 V, step-down 5 V LM2596.
- **Control:** Placa Olivia, TRIAC resistencia 200 W, ventilador y luz, bomba, puente H L298, motor de volteo, BME280, reeds, tierra y prensacables.

## 9. Mapa de señales
- **GPIO2** → VOLTEO_UP / IN_A_N
- **GPIO15** → VOLTEO_DOWN / IN_A_P
- **GPIO13** → VOLTEO_EN / EN_A
- **GPIO14** → resistencia
- **GPIO17** → humidificador
- **GPIO35** → reed superior
- **GPIO34** → reed inferior
- **GPIO32/33** → BME280 I²C

## 10. Puesta en marcha (Checklist)
- [ ] Inspección mecánica sin tensión.
- [ ] Continuidad y tierra.
- [ ] Separación AC/DC.
- [ ] Primer encendido sin cargas.
- [ ] Prueba de fuente 12 V y 5 V (ajustar LM2596).
- [ ] Verificación lectura BME280.
- [ ] Activación de resistencia.
- [ ] Activación de ventilador/luz.
- [ ] Activación de bomba.
- [ ] Volteo manual.
- [ ] Lectura de reeds (finales de carrera).
- [ ] Ciclo completo sin huevos.

## 11. Troubleshooting
- **No enciende:** Revisar entrada de 220V, disyuntor, termomagnéticas y fusibles de placa Olivia.
- **No mide temp/humedad:** Verificar conexión I2C (GPIO32/33) y alimentación del BME280.
- **No calienta:** Comprobar salida TRIAC (GPIO14), resistencia de 200W, y cableado de potencia.
- **No humidifica:** Revisar salida hacia bomba (GPIO17), nivel de agua.
- **No gira:** Verificar motorreductor, puente H L298 (GPIO13, GPIO2, GPIO15), o atasco mecánico.
- **Gira al revés:** Invertir cables del motor o lógica en firmware.
- **No detecta reed:** Probar continuidad del sensor al acercar imán, verificar pull-up en GPIO34/35.
- **Se traba el volteo:** Aflojar correa, alinear bujes PTFE y verificar roce en bandejas (**VER CAD**).

## 12. Anexos
- **Inventario CAD:** (Ver tabla en sección 4).
- **Nota del CAD maestro:** El modelo no está versionado binariamente en el repositorio Git. Asegurarse de tener el `Incubadora-Final.3dm` correcto antes de extraer datos.
