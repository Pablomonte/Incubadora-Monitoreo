# Incubadora LibreIncu — rediseño «Incubadora-Final»

Documentación de fabricación del **nuevo diseño** de la incubadora, generada a partir del
CAD maestro (`Rediseno/Incubadora-Final.3dm`).

!!! info "Cómo leer esta documentación"
    Las dimensiones mecánicas provienen del **bounding box (envolvente)** de cada pieza del CAD.
    Sirven para **comprar y cortar**, no para ubicar agujeros, plegados ni ángulos. Donde haga
    falta geometría fina, el texto indica **`VER CAD`**.

## Secciones

- **[Manual de montaje](manual.md)** — alcance, BOM consolidada, preparación de piezas,
  montaje mecánico, sistema de volteo, instalación eléctrica, mapa de señales,
  puesta en marcha y troubleshooting.
- **[Inventario CAD](inventario.md)** — inventario mecánico completo y trazable,
  con lista de corte/compra por pieza.

## El rediseño de un vistazo

- **Envolvente de sólidos:** ≈ 605 × 1264 × 1189 mm.
- **Estructura:** bastidor de tubo 25×25 y 30×30 mm.
- **Cerramiento:** chapa 1/8″ (~3 mm), MDF 18 mm y frente de policarbonato.
- **Volteo:** polea dentada + correa, rodamientos 624/626/HLM8UU, buje PTFE, acoples PA6.
- **Control:** placa Olivia v0.2 (ESP32-WROOM-32D).

!!! note "Sobre el CAD maestro"
    Los binarios `.3dm/.stp/.igs` (~515 MB) **no** están versionados en git. El inventario se
    regenera con `python3 Rediseno/extract_cad.py` (requiere `rhino3dm`).
