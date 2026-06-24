# Montaje mecanico por componentes

Cada componente se muestra con dos vistas: **locator** para ubicarlo en la incubadora y **solo** para entender que lo compone. Las mini-BOMs se generan desde el inventario CAD.

!!! tip "Orden recomendado"
    Montar primero cajon, luego contrafondo, mecanismo de rotación, transmision, bandejas y puerta. Dejar actuadores/electrica para despues de validar que la mecanica se mueve libremente.

## Cajon y estructura

![Locator cajon](img/componentes/cajon-locator.png){ width=560 }
![Subconjunto cajon](img/componentes/cajon-solo.png){ width=420 }

--8<-- "cad/componentes/cajon.md"

**Pasos**

1. Cortar y desbarbar perfiles.
2. Armar el marco sobre superficie plana.
3. Presentar piezas de union y chapa caja antes de fijar definitivamente.
4. Fijar o soldar manteniendo escuadra.

**Control de calidad**

- Diagonales iguales.
- Sin torsion visible.
- Base estable en cuatro apoyos.

**Riesgos / VER CAD**

- Las piezas `30x122x143` y la chapa caja requieren orientacion y encuentros desde CAD.

## Contrafondo y cerramientos

![Locator contrafondo](img/componentes/contrafondo-locator.png){ width=560 }
![Subconjunto contrafondo](img/componentes/contrafondo-solo.png){ width=420 }

--8<-- "cad/componentes/contrafondo.md"

**Pasos**

1. Presentar MDF y chapas sobre la estructura.
2. Verificar interferencias con puerta, bandejas y mecanismo de rotación.
3. Marcar perforaciones con CAD abierto.
4. Fijar paneles evitando fugas de aire.

**Control de calidad**

- Paneles planos y sin alabeo.
- Juntas cerradas.
- Ningun borde cortante expuesto.

**Riesgos / VER CAD**

- Plegados de chapa y posiciones de agujeros no salen de la medida exterior.

## Mecanismo de rotación

![Locator mecanismo de rotación](img/componentes/rotacion-locator.png){ width=560 }
![Subconjunto mecanismo de rotación](img/componentes/rotacion-solo.png){ width=420 }

--8<-- "cad/componentes/rotacion.md"

**Pasos**

1. Montar rodamientos en alojamientos.
2. Presentar ejes, bujes y acoples sin apretar.
3. Alinear el conjunto y rotar manualmente.
4. Ajustar acoples cuando no haya roce ni punto duro.

**Control de calidad**

- Rotación suave a mano.
- Rodamientos asentados.
- Acoples centrados.

**Riesgos / VER CAD**

- Alojamiento de rodamientos, posicion de eje y acoples requieren CAD.

## Transmision y guiado

![Locator transmision](img/componentes/transmision-locator.png){ width=560 }
![Subconjunto transmision](img/componentes/transmision-solo.png){ width=420 }

--8<-- "cad/componentes/transmision.md"

**Pasos**

1. Presentar guia y cremallera.
2. Verificar engrane con la polea dentada.
3. Fijar provisoriamente y recorrer el movimiento completo.
4. Ajustar posicion antes de fijar definitivamente.

**Control de calidad**

- Engrane continuo.
- Sin salto de diente.
- Sin roce lateral.

**Riesgos / VER CAD**

- Posicion de cremallera y guia es critica para que la rotación no se trabe.

## Bandejas y bastidor giratorio

![Locator bandejas](img/componentes/bandejas-locator.png){ width=560 }
![Subconjunto bandejas](img/componentes/bandejas-solo.png){ width=420 }

--8<-- "cad/componentes/bandejas.md"

**Pasos**

1. Montar bandejas fijas y hombros.
2. Presentar bandejas hueveras.
3. Vincular bandejas al eje mediante acoples bandeja-eje.
4. Probar recorrido manual completo.

**Control de calidad**

- Bandejas niveladas.
- Hueveras firmes.
- Recorrido sin tocar cerramientos.

**Riesgos / VER CAD**

- La bandeja huevera se registra como instancia; validar geometria en CAD antes de fabricar o reemplazar.

## Puerta

![Locator puerta](img/componentes/puerta-locator.png){ width=560 }
![Subconjunto puerta](img/componentes/puerta-solo.png){ width=420 }

--8<-- "cad/componentes/puerta.md"

**Pasos**

1. Presentar marco, frente de policarbonato, tapas y bisagras.
2. Ajustar apertura antes de colocar burletes o cepillos.
3. Verificar cierre parejo.
4. Fijar ventilacion de puerta.

**Control de calidad**

- Cierre sin luz.
- Bisagras alineadas.
- Frente sin tension ni fisuras.

**Riesgos / VER CAD**

- Confirmar agujeros y ventilacion con CAD.

## Actuadores mecanicos y soportes electricos

![Locator actuadores](img/componentes/electrica-locator.png){ width=560 }
![Subconjunto actuadores](img/componentes/electrica-solo.png){ width=420 }

--8<-- "cad/componentes/electrica.md"

**Nota**

Esta seccion solo ubica elementos fisicos como cooler, bomba y soportes. El cableado se documenta en Instalacion electrica.
