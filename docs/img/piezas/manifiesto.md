# Manifiesto de renders de piezas

- **aceptacion_completa:** `True`
- **metodo:** rhino3dm_native_meshes
- **gmsh:** Envolvente OK: 608.7 x 1213.0 x 1063.9 mm
- **match centroides:** {'matched': 10968, 'ambiguous': 4199, 'total_entities': 15167}

| Pieza | Slug | Estado | Triangulos | Dim mm | Motivo |
|---|---|---|---|---|---|
| Perfil25-25 | perfil25-25 | rendered | 13259 | 577x668x1086 | renderizado desde mallas nativas de rhino3dm |
| Chapa 1/8 | chapa-1-8 | rendered | 18380 | 125x255x298 | renderizado desde mallas nativas de rhino3dm |
| Chapa-SoporteInferior | chapa-soporteinferior | rendered | 1566 | 24x486x504 | renderizado desde mallas nativas de rhino3dm |
| MDF18mm | mdf18mm | rendered | 7176 | 601x784x1169 | renderizado desde mallas nativas de rhino3dm |
| ChapaCooler | chapacooler | rendered | 5247 | 170x232x461 | renderizado desde mallas nativas de rhino3dm |
| Chapa-Paredon | chapa-paredon | rendered | 8080 | 291x359x407 | renderizado desde mallas nativas de rhino3dm |
| FRENTE-PC | frente-pc | rendered | 4744 | 20x486x1189 | renderizado desde mallas nativas de rhino3dm |
| MDF55 | mdf55 | rendered | 1436 | 169x497x1021 | renderizado desde mallas nativas de rhino3dm |
| Chapa-Caja | chapa-caja | rendered | 3980 | 85x333x459 | renderizado desde mallas nativas de rhino3dm |
| Tapas | tapas | rendered | 2164 | 15x465x783 | renderizado desde mallas nativas de rhino3dm |
| U 2219 - Door | u-2219---door | rendered | 8172 | 26x542x1015 | renderizado desde mallas nativas de rhino3dm |
| BisagraP | bisagrap | rendered | 2496 | 35x35x669 | renderizado desde mallas nativas de rhino3dm |
| VentilacionDoor | ventilaciondoor | rendered | 19720 | 22x31x422 | renderizado desde mallas nativas de rhino3dm |
| huevera | huevera | rendered | 1217 | 24x361x392 | renderizado desde mallas nativas de rhino3dm |
| BandejasFijas | bandejasfijas | rendered | 15998 | 260x480x481 | renderizado desde mallas nativas de rhino3dm |
| HombroBandej | hombrobandej | rendered | 58332 | 33x329x454 | renderizado desde mallas nativas de rhino3dm |
| AcopleBandejaEje | acoplebandejaeje | rendered | 118914 | 19x308x530 | renderizado desde mallas nativas de rhino3dm |
| ACOPLE 8 a 5 | acople-8-a-5 | rendered | 295376 | 426x467x486 | renderizado desde mallas nativas de rhino3dm |
| Cremayera | cremayera | rendered | 23672 | 24x65x347 | renderizado desde mallas nativas de rhino3dm |
| AcoplesPA6 | acoplespa6 | rendered | 6794 | 6x27x264 | renderizado desde mallas nativas de rhino3dm |
| GUIA-CREMA | guia-crema | rendered | 4194 | 21x63x320 | renderizado desde mallas nativas de rhino3dm |
| Barra Avance Z | barra-avance-z | rendered | 552494 | 8x30x132 | renderizado desde mallas nativas de rhino3dm |
| Buje-PTFE | buje-ptfe | rendered | 1036 | 12x16x311 | renderizado desde mallas nativas de rhino3dm |
| FondoBrazo | fondobrazo | rendered | 9760 | 40x329x464 | renderizado desde mallas nativas de rhino3dm |
| PoleaDentada | poleadentada | rendered | 3928 | 33x50x50 | renderizado desde mallas nativas de rhino3dm |
| SoporT-AntiVib | soport-antivib | rendered | 2968 | 29x64x73 | renderizado desde mallas nativas de rhino3dm |
| BASE | base | rendered | 197582 | 588x695x1170 | renderizado desde mallas nativas de rhino3dm |
| BoquillaAltaP | boquillaaltap | rendered | 13292 | 29x50x59 | renderizado desde mallas nativas de rhino3dm |
| HerrajesTraseros | herrajestraseros | rendered | 7668 | 38x381x589 | renderizado desde mallas nativas de rhino3dm |
| SeparadorPAI | separadorpai | rendered | 3376 | 4x75x90 | renderizado desde mallas nativas de rhino3dm |

## Omitidos del conjunto

| Capa | Motivo |
|---|---|
| huevera | instancia de bloque (sin malla) |
| AcopleBandejaEje | acople repetido (no estructural) |
| ACOPLE 8 a 5 | acople repetido (no estructural) |
| AcoplesPA6 | acople repetido (no estructural) |
| Barra Avance Z | pieza secundaria/pequena |
| Buje-PTFE | pieza secundaria/pequena |
| FondoBrazo | pieza secundaria/pequena |
| SoporT-AntiVib | pieza secundaria/pequena |
| BASE | grupo BASE (objetos sueltos, no estructural) |
| BoquillaAltaP | pieza secundaria/pequena |
| HerrajesTraseros | pieza secundaria/pequena |
| SeparadorPAI | pieza secundaria/pequena |
