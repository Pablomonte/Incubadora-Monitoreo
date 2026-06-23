# Vista 3D y despiece

Explorá el modelo 3D de la LibreIncu-150 directamente en el navegador. Podés rotar con el mouse/tactil,
usar el boton para alternar entre **armado** y **despiece**, y hacer clic en las piezas de abajo para
ver cada una en 3D. Los numeros (`Nº`) coinciden con la tabla del [Inventario CAD](inventario.md).

!!! info "Requisitos"
    Esta pagina usa `<model-viewer>` embebido en el sitio. Necesita un navegador con WebGL.
    No aparece en el PDF. Los modelos se descargan bajo demanda; el poster PNG se muestra hasta entonces.

!!! warning "Modelos 3D = solo visualizacion"
    Los GLB se generan a partir de mallas simplificadas para web. **No usarlos para medir ni fabricar:**
    pierden detalle fino (agujeros, dientes, plegados). Las medidas y la geometria de taller estan en el
    [Inventario CAD](inventario.md) y en el CAD maestro.

<script type="module" src="../assets/model-viewer.min.js"></script>

## Conjunto

<div class="vista3d-conjunto">
  <div class="v3d-tabs">
    <button id="btn-armado" class="v3d-tab active" data-mode="armado">Armado</button>
    <button id="btn-despiece" class="v3d-tab" data-mode="despiece">Despiece</button>
  </div>
  <model-viewer id="visor-conjunto"
                src="../models/conjunto-armado.glb"
                poster="../img/piezas/_conjunto.png"
                alt="Conjunto LibreIncu-150"
                camera-controls
                camera-orbit="-60deg 22deg auto"
                auto-rotate
                reveal="auto"
                shadow-intensity="1"
                exposure="0.8">
    <button slot="hotspot-cajon" data-position="1036.0455851859317 573.5805785563466 -213.636739024928" data-normal="0.0 1.0 0.0">Cajon y estructura</button>
    <button slot="hotspot-contrafondo" data-position="999.2311372930535 616.6499866863312 -366.61094505836934" data-normal="0.0 1.0 0.0">Contrafondo y cerramientos</button>
    <button slot="hotspot-rotacion" data-position="969.2155849818809 694.4141909870903 -311.40755386204756" data-normal="0.0 1.0 0.0">Mecanismo de giro (ejes, acoples, rodamientos)</button>
    <button slot="hotspot-transmision" data-position="1000.4258113050034 735.2830899136111 -405.75391387767877" data-normal="0.0 1.0 0.0">Transmision y guiado</button>
    <button slot="hotspot-bandejas" data-position="1065.0036877691173 654.4253364751215 -219.839055861182" data-normal="0.0 1.0 0.0">Bandejas y bastidor giratorio</button>
    <button slot="hotspot-puerta" data-position="803.9216353371061 681.8146624351087 171.2765695904704" data-normal="0.0 1.0 0.0">Puerta</button>
    <button slot="hotspot-electrica" data-position="993.3398209865012 572.5378743549082 -322.17177692953413" data-normal="0.0 1.0 0.0">Actuadores y electrica</button>
    <div slot="poster" class="v3d-poster-hint">Toca o hace clic para cargar el modelo 3D</div>
    <div class="v3d-fallback">
      <img src="../img/piezas/_conjunto.png" alt="Conjunto LibreIncu-150">
      <p>Cargando visor 3D... Si no aparece, comproba tu conexion o usa un navegador con WebGL.</p>
    </div>
  </model-viewer>
</div>

## Piezas

Selecciona una pieza para ver su modelo 3D. Los numeros son los mismos del [Inventario CAD](inventario.md).

<div class="vista3d-pieza">
  <model-viewer id="visor-pieza"
                src=""
                poster="../img/piezas/_conjunto.png"
                alt="Pieza seleccionada"
                camera-controls
                camera-orbit="-60deg 22deg auto"
                reveal="auto"
                shadow-intensity="1"
                exposure="0.8">
    <div slot="poster" class="v3d-poster-hint">Selecciona una pieza de la grilla</div>
    <div class="v3d-fallback">
      <img src="../img/piezas/_conjunto.png" alt="Selecciona una pieza">
      <p>Cargando visor 3D... Si no aparece, comproba tu conexion o usa un navegador con WebGL.</p>
    </div>
  </model-viewer>
  <div id="pieza-caption" class="v3d-caption">Ninguna pieza seleccionada</div>
</div>

--8<-- "cad/vista3d_piezas.md"

<script>
(function() {
  const visorConjunto = document.getElementById('visor-conjunto');
  const btnArmado = document.getElementById('btn-armado');
  const btnDespiece = document.getElementById('btn-despiece');
  const visorPieza = document.getElementById('visor-pieza');
  const caption = document.getElementById('pieza-caption');

  function setConjunto(mode) {
    const src = mode === 'armado' ? '../models/conjunto-armado.glb' : '../models/conjunto-despiece.glb';
    visorConjunto.src = src;
    btnArmado.classList.toggle('active', mode === 'armado');
    btnDespiece.classList.toggle('active', mode === 'despiece');
  }

  btnArmado.addEventListener('click', () => setConjunto('armado'));
  btnDespiece.addEventListener('click', () => setConjunto('despiece'));

  document.getElementById('vista3d-grid').addEventListener('click', function(e) {
    const thumb = e.target.closest('.v3d-thumb');
    if (!thumb || thumb.classList.contains('v3d-thumb-no3d')) return;
    visorPieza.src = thumb.dataset.src;
    visorPieza.poster = thumb.dataset.poster;
    caption.textContent = thumb.dataset.caption;
    document.querySelectorAll('.v3d-thumb').forEach(b => b.classList.remove('active'));
    thumb.classList.add('active');
  });
})();
</script>

<style>
.vista3d-conjunto, .vista3d-pieza {
  margin: 1rem 0;
}
.v3d-tabs {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}
.v3d-tab {
  padding: 0.4rem 0.8rem;
  border: 1px solid #ccc;
  background: #f5f5f5;
  cursor: pointer;
}
.v3d-tab.active {
  background: #2e7d32;
  color: #fff;
  border-color: #2e7d32;
}
model-viewer {
  width: 100%;
  height: 480px;
  background: #fafafa;
}
.v3d-poster-hint {
  position: absolute;
  bottom: 1rem;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0,0,0,0.6);
  color: #fff;
  padding: 0.3rem 0.6rem;
  border-radius: 4px;
  font-size: 0.85rem;
  pointer-events: none;
}
.v3d-fallback {
  padding: 1rem;
  color: #666;
}
.v3d-caption {
  text-align: center;
  font-weight: 500;
  margin-top: 0.5rem;
}
.vista3d-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 0.75rem;
  margin-top: 1rem;
}
.v3d-thumb {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.5rem;
  border: 1px solid #ddd;
  background: #fff;
  cursor: pointer;
  transition: border-color 0.2s;
}
.v3d-thumb:hover, .v3d-thumb.active {
  border-color: #2e7d32;
}
.v3d-thumb-no3d {
  cursor: default;
  opacity: 0.7;
  background: #f0f0f0;
}
.v3d-thumb img {
  width: 100%;
  height: 120px;
  object-fit: contain;
  background: #fafafa;
}
.v3d-thumb span {
  margin-top: 0.4rem;
  font-size: 0.8rem;
  text-align: center;
  line-height: 1.2;
}
model-viewer:defined .v3d-fallback {
  display: none;
}
.v3d-fallback {
  text-align: center;
  padding: 1rem;
  color: #666;
}
.v3d-fallback img {
  max-width: 100%;
  max-height: 360px;
  object-fit: contain;
  background: #fafafa;
}
</style>
