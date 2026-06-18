# Inventario mecanico extraido del CAD maestro

- **Modelo:** `Incubadora-Final.3dm` (Rhino, unidades **mm**)
- **Envolvente total:** 604.8 x 1263.9 x 1189.2 mm (ancho x prof x alto aprox.)
- **Tamanos = bounding box (envolvente).** No son cotas de agujeros, plegados ni angulos: para geometria fina **abrir el CAD**.
- Notacion de tamanos: `seccion_menor x seccion_media x largo (xN)`, una entrada por cada medida distinta dentro de la pieza.


## Estructura

| Pieza | Ruta CAD | Cant | Tamanos envolventes mm | Material / nota | Fabricacion | Confianza |
|---|---|---|---|---|---|---|
| Perfil25-25 | Perfil25-25 | 20 | 30x30x1086 (x4); 25x25x934 (x1); 25x25x654 (x4); 25x25x609 (x1); 30x30x577 (x4); 40x40x461 (x1); 25x25x448 (x1); 25x25x406 (x1); 25x25x191 (x1); 30x122x143 (x2) | Tubo estructural 25x25 (la capa tambien incluye perfiles 30x30) | cortar | envolvente |

## Cerramiento

| Pieza | Ruta CAD | Cant | Tamanos envolventes mm | Material / nota | Fabricacion | Confianza |
|---|---|---|---|---|---|---|
| Chapa 1/8 | Chapa 1/8 | 8 | 3x22x261 (x1); 3x88x122 (x1); 4x90x108 (x1); 4x39x92 (x1); 4x46x90 (x1); 4x43x83 (x2); 3x58x77 (x1) | Chapa 1/8" (~3.2 mm) | cortar + plegar (VER CAD) | envolvente |
| Chapa-SoporteInferior | Chapa-SoporteInferior | 4 | 24x24x504 (x2); 24x24x486 (x1); 1x192x468 (x1) | Chapa metalica plegada | cortar + plegar (VER CAD) | envolvente |
| MDF18mm | MDF18mm | 4 | 22x784x1169 (x2); 22x601x659 (x1); 18x501x654 (x1) | Tablero MDF 18 mm | cortar tablero (VER CAD) | envolvente |
| ChapaCooler | ChapaCooler | 3 | 170x232x461 (x1); 0x12x16 (x1); 0x4x5 (x1) | Chapa metalica plegada | cortar + plegar (VER CAD) | envolvente |
| Chapa-Paredon | Chapa-Paredon | 2 | 53x163x379 (x1); 264x291x359 (x1) | Chapa metalica plegada | cortar + plegar (VER CAD) | envolvente |
| FRENTE-PC | FRENTE-PC | 2 | 5x486x1189 (x2) |  | cortar tablero (VER CAD) | envolvente |
| MDF55 | MDF55 | 2 | 6x497x1021 (x1); 7x472x982 (x1) | Tablero MDF | cortar tablero (VER CAD) | envolvente |
| Chapa-Caja | Chapa-Caja | 1 | 85x333x459 (x1) | Chapa metalica plegada | cortar + plegar (VER CAD) | envolvente |

## Puerta

| Pieza | Ruta CAD | Cant | Tamanos envolventes mm | Material / nota | Fabricacion | Confianza |
|---|---|---|---|---|---|---|
| Tapas | Tapas | 4 | 11x277x387 (x1); 6x241x332 (x1); 11x168x173 (x1); 6x150x154 (x1) |  | VER CAD | envolvente |
| U 2219 - Door | U 2219 - Door | 4 | 23x26x1015 (x2); 23x26x542 (x2) |  | VER CAD | envolvente |
| BisagraP | BisagraP | 4 | 8x35x76 (x4) |  | VER CAD | envolvente |
| Cremayera | Cremayera | 4 | 24x64x213 (x1); 24x65x165 (x1); 4x4x11 (x2) |  | VER CAD | envolvente |
| VentilacionDoor | VentilacionDoor | 2 | 22x22x31 (x2) |  | VER CAD | envolvente |

## Bandeja

| Pieza | Ruta CAD | Cant | Tamanos envolventes mm | Material / nota | Fabricacion | Confianza |
|---|---|---|---|---|---|---|
| AcopleBandejaEje | AcopleBandejaEje | 75 | 19x19x55 (x6); 8x8x48 (x12); 19x19x39 (x3); 12x19x19 (x12); 2x14x14 (x30); 0x9x9 (x12) | Nylon PA6 (mecanizado) | mecanizar / imprimir (VER CAD) | envolvente |
| huevera | Bandeja::huevera | 23 | 23 bloque(s) sin explotar |  | VER CAD | instancia (VER CAD) |
| BandejasFijas | BandejasFijas | 15 | 18x18x481 (x6); 18x18x480 (x3); 16x98x98 (x6) |  | VER CAD | envolvente |
| HombroBandej | HombroBandej | 6 | 14x33x89 (x6) |  | VER CAD | envolvente |
| GUIA-CREMA | GUIA-CREMA | 3 | 11x11x317 (x1); 14x21x63 (x2) |  | VER CAD | envolvente |

## Volteo

| Pieza | Ruta CAD | Cant | Tamanos envolventes mm | Material / nota | Fabricacion | Confianza |
|---|---|---|---|---|---|---|
| ACOPLE 8 a 5 | ACOPLE 8 a 5 | 17 | 7x18x310 (x1); 8x8x30 (x2); 6x13x15 (x2); 2x6x6 (x10); 2x5x5 (x2) |  | mecanizar / imprimir (VER CAD) | envolvente |
| Rodamiento626 | Rodamiento626 | 11 | 6x19x19 (x11) | Rodamiento 626 - 6x19x6 mm (comercial) | comprar | estandar |
| Rodamiento624 | Rodamiento624 | 3 | 5x13x13 (x3) | Rodamiento 624 - 4x13x5 mm (comercial) | comprar | estandar |
| AcoplesPA6 | AcoplesPA6 | 3 | 6x27x31 (x1); 6x24x31 (x2) | Nylon PA6 (mecanizado) | mecanizar / imprimir (VER CAD) | envolvente |
| Barra Avance Z | Barra Avance Z | 2 | 8x8x30 (x2) |  | VER CAD | envolvente |
| Buje-PTFE | Buje-PTFE | 2 | 2x4x311 (x1); 4x5x5 (x1) | PTFE (mecanizado) | mecanizar / imprimir (VER CAD) | envolvente |
| FondoBrazo | FondoBrazo | 2 | 6x40x329 (x2) |  | VER CAD | envolvente |
| RodamientoHLM8UU | RodamientoHLM8UU | 1 | 19x19x54 (x1) | Rodamiento lineal LM8UU (comercial) | comprar | estandar |
| PoleaDentada | PoleaDentada | 1 | 33x50x50 (x1) | Polea dentada | mecanizar / imprimir (VER CAD) | envolvente |
| SoporT-AntiVib | SoporT-AntiVib | 1 | 29x64x73 (x1) |  | VER CAD | envolvente |

## Fijacion

| Pieza | Ruta CAD | Cant | Tamanos envolventes mm | Material / nota | Fabricacion | Confianza |
|---|---|---|---|---|---|---|
| TuercasM6 | TuercasM6 | 82 | 11x14x14 (x39); 8x10x10 (x5); 1x7x7 (x33); 1x5x5 (x5) | Fijacion comercial | comprar | estandar |
| Tornillo M3 | Tornillo M3 | 27 | 3x3x25 (x4); 3x3x23 (x4); 3x3x16 (x3); 3x3x15 (x3); 3x3x12 (x3); 3x3x10 (x3); 1x5x5 (x7) | Fijacion comercial | comprar | estandar |
| Tornillo M5 | Tornillo M5 | 24 | 6x6x48 (x4); 6x6x44 (x4); 6x6x26 (x4); 6x6x24 (x4); 3x10x10 (x8) | Fijacion comercial | comprar | estandar |
| Tornillo M4 | Tornillo M4 | 18 | 4x4x30 (x4); 4x4x24 (x6); 4x4x20 (x2); 2x7x7 (x6) | Fijacion comercial | comprar | estandar |
| Tuercas M3 | Tuercas M3 | 11 | 3x9x9 (x11) | Fijacion comercial | comprar | estandar |
| Tuercas M5 | Tuercas M5 | 8 | 4x12x12 (x8) | Fijacion comercial | comprar | estandar |
| Tuercas M4 | Tuercas M4 | 5 | 3x12x12 (x5) | Fijacion comercial | comprar | estandar |
| Tuercas M8 | Tuercas M8 | 2 | 7x16x16 (x2) | Fijacion comercial | comprar | estandar |

## Comercial

| Pieza | Ruta CAD | Cant | Tamanos envolventes mm | Material / nota | Fabricacion | Confianza |
|---|---|---|---|---|---|---|
| BombaStuff | BombaStuff | 10 | 108x109x240 (x1); 162x168x208 (x1); 65x104x124 (x1); 67x85x121 (x1); 14x111x111 (x1); 2x107x107 (x2); 58x66x67 (x1); 38x39x57 (x1); 26x37x37 (x1) | Bomba (comercial) | comprar | envolvente |
| Cooler | Cooler | 1 | 154x174x204 (x1) | Ventilador / cooler (comercial) | comprar | envolvente |

## Otro

| Pieza | Ruta CAD | Cant | Tamanos envolventes mm | Material / nota | Fabricacion | Confianza |
|---|---|---|---|---|---|---|
| BASE | BASE | 60 | 8x22x1170 (x2); 8x22x588 (x2); 0x330x456 (x1); 108x252x372 (x1); 3x90x264 (x1); 30x46x139 (x2); 48x96x132 (x1); 98x112x126 (x1); 18x108x120 (x1); 41x48x108 (x1); 22x48x96 (x3); 7x28x95 (x1); 7x29x67 (x1); 18x48x60 (x1); 41x45x54 (x1); 18x24x48 (x1); 18x48x48 (x1); 19x38x44 (x1); 12x18x38 (x1); 19x19x28 (x3); 24x24x25 (x1); 13x13x16 (x5); 10x10x16 (x15); 14x14x16 (x2); 2x14x14 (x9); 1 bloque(s) sin explotar |  | VER CAD | envolvente |
| BoquillaAltaP | BoquillaAltaP | 5 | 18x20x50 (x1); 17x17x44 (x1); 11x11x28 (x1); 10x10x16 (x2) |  | VER CAD | envolvente |
| HerrajesTraseros | HerrajesTraseros | 3 | 6x38x136 (x2); 6x38x113 (x1) |  | VER CAD | envolvente |
| SeparadorPAI | SeparadorPAI | 1 | 4x75x90 (x1) |  | VER CAD | envolvente |

## Visual

| Pieza | Ruta CAD | Cant | Tamanos envolventes mm | Material / nota | Fabricacion | Confianza |
|---|---|---|---|---|---|---|
| Pelos | Pelos | 780 | 780 bloque(s) sin explotar |  | no fabricable (referencia visual) | instancia (VER CAD) |
| Auxiliar1 | Auxiliar1 | 32 | 4x53x488 (x2); 22x24x148 (x2); 22x78x90 (x2); 22x53x65 (x2); 23x24x60 (x2); 19x29x38 (x1); 13x13x16 (x2); 1x12x12 (x8); 1x10x10 (x4); 1x9x9 (x7) |  | no fabricable (referencia visual) | envolvente |
| Reguetones | Reguetones | 14 | 23x48x48 (x6); 11x11x40 (x4); 2x22x22 (x4) |  | no fabricable (referencia visual) | envolvente |
| Letritas | Letritas | 10 | 0x20x22 (x1); 0x3x20 (x1); 0x15x20 (x4); 0x13x20 (x1); 0x11x20 (x1); 0x10x20 (x1); 0x17x20 (x1) |  | no fabricable (referencia visual) | envolvente |
| Auxiliar2 | Auxiliar2 | 1 | 43x43x121 (x1) |  | no fabricable (referencia visual) | envolvente |
| Auxiliar3 | Auxiliar3 | 1 | 29x71x73 (x1) |  | no fabricable (referencia visual) | envolvente |
