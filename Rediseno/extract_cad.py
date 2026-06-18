import json
import csv
import os
import rhino3dm

def get_layer_path(layer_index, layers):
    if layer_index < 0 or layer_index >= len(layers):
        return "Unknown"
    
    layer = layers[layer_index]
    path = [layer.Name]
    parent_id = layer.ParentLayerId
    
    # Simple loop to trace back to root (assuming rhino3dm layers have Id and ParentLayerId)
    # rhino3dm Layer has: Id, ParentLayerId, Name
    # We need to find the parent layer by Id.
    while parent_id != "00000000-0000-0000-0000-000000000000" and parent_id is not None:
        found = False
        for l in layers:
            if l.Id == parent_id:
                path.insert(0, l.Name)
                parent_id = l.ParentLayerId
                found = True
                break
        if not found:
            break
            
    return "::".join(path)

def infer_material(name, layer_path):
    lname = (name + " " + layer_path).lower()
    if "perfil25-25" in lname: return "tubo 25x25"
    if "chapa 1/8" in lname: return "chapa 1/8\""
    if "acoplespa6" in lname or "acople" in lname and "pa6" in lname: return "PA6"
    if "buje-ptfe" in lname: return "PTFE"
    if "rodamiento" in lname or "624" in lname or "626" in lname or "hlm8uu" in lname: return "comercial"
    if "tornillo" in lname or "m3" in lname or "m4" in lname or "m5" in lname: return "fijación comercial"
    if "motor" in lname or "reductor" in lname: return "comercial"
    return "Desconocido"

def classify_usage(name, layer_path):
    lname = (name + " " + layer_path).lower()
    if "bastidor" in lname or "perfil" in lname or "estructura" in lname: return "estructura"
    if "chapa" in lname or "gabinete" in lname or "cerramiento" in lname: return "cerramiento"
    if "puerta" in lname or "bisagra" in lname: return "puerta"
    if "bandeja" in lname or "guia" in lname or "cremallera" in lname: return "bandeja"
    if "volteo" in lname or "motor" in lname or "eje" in lname or "polea" in lname or "correa" in lname or "acople" in lname: return "volteo"
    if "tornillo" in lname or "tuerca" in lname or "arandela" in lname or "fijacion" in lname: return "fijacion"
    if "electrico" in lname or "cable" in lname or "placa" in lname or "fuente" in lname or "sensor" in lname: return "electrico"
    return "otro"

def classify_fabrication(name, material, layer_path):
    lname = (name + " " + material + " " + layer_path).lower()
    if "comercial" in material: return "comercial (comprar)"
    if "tubo" in material: return "cortar"
    if "chapa" in material:
        if "plegad" in lname: return "plegar"
        return "cortar"
    if "pa6" in material: return "mecanizar"
    if "ptfe" in material: return "mecanizar"
    if "impres" in lname or "3d" in lname or "pla" in lname or "petg" in lname or "abs" in lname: return "imprimir"
    return "ver_CAD"

def get_confidence(fab_level):
    if fab_level in ["comercial (comprar)", "cortar", "imprimir"]: return "envolvente"
    if fab_level in ["mecanizar", "plegar"]: return "insuficiente"
    return "exacta" # Default fallback, though in this context almost all might be envolvente/insuficiente

def main():
    model_path = "Incubadora-Final.3dm"
    if not os.path.exists(model_path):
        print(f"File not found: {model_path}")
        return
        
    model = rhino3dm.File3dm.Read(model_path)
    
    layers = []
    for l in model.Layers:
        layers.append(l)
        
    materials = []
    for m in model.Materials:
        materials.append(m)

    objects_data = []
    
    for obj in model.Objects:
        attr = obj.Attributes
        geom = obj.Geometry
        
        layer_path = get_layer_path(attr.LayerIndex, layers)
        
        bb = geom.GetBoundingBox()
        dims = [bb.Max.X-bb.Min.X, bb.Max.Y-bb.Min.Y, bb.Max.Z-bb.Min.Z]
        center = [(bb.Max.X+bb.Min.X)/2, (bb.Max.Y+bb.Min.Y)/2, (bb.Max.Z+bb.Min.Z)/2]
        
        name = attr.Name if attr.Name else "Unnamed"
        
        mat_name = "Default"
        if attr.MaterialIndex >= 0 and attr.MaterialIndex < len(materials):
            mat_name = materials[attr.MaterialIndex].Name
            
        objects_data.append({
            "id": str(attr.Id),
            "name": name,
            "layer_path": layer_path,
            "geometry_type": str(geom.ObjectType),
            "bounding_box_mm": {"min": [bb.Min.X, bb.Min.Y, bb.Min.Z], "max": [bb.Max.X, bb.Max.Y, bb.Max.Z]},
            "dimensions_mm": [round(d, 2) for d in dims],
            "center_mm": [round(c, 2) for c in center],
            "material_rhino": mat_name
        })

    # Group by layer/piece (we'll group by layer_path and name)
    groups = {}
    for obj in objects_data:
        key = f"{obj['layer_path']} - {obj['name']}"
        if key not in groups:
            material_inferred = infer_material(obj['name'], obj['layer_path'])
            uso = classify_usage(obj['name'], obj['layer_path'])
            fab_level = classify_fabrication(obj['name'], material_inferred, obj['layer_path'])
            confianza = get_confidence(fab_level)
            
            groups[key] = {
                "layer_path": obj['layer_path'],
                "name": obj['name'],
                "count": 0,
                "dimensions_mm": obj['dimensions_mm'],
                "material": material_inferred,
                "uso": uso,
                "fabricacion": fab_level,
                "confianza": confianza,
                "objects": []
            }
        groups[key]["count"] += 1
        groups[key]["objects"].append(obj["id"])
        
        # Expand bounding box dimensions if new items are bigger (naive approach, typically we'd merge BBs but here we just keep max dims to get an idea)
        groups[key]["dimensions_mm"] = [
            max(groups[key]["dimensions_mm"][0], obj['dimensions_mm'][0]),
            max(groups[key]["dimensions_mm"][1], obj['dimensions_mm'][1]),
            max(groups[key]["dimensions_mm"][2], obj['dimensions_mm'][2])
        ]

    # Convert dict to list
    inventory = list(groups.values())
    
    os.makedirs("cad", exist_ok=True)
    
    with open("cad/inventario.json", "w", encoding="utf-8") as f:
        json.dump(inventory, f, indent=2, ensure_ascii=False)
        
    with open("cad/inventario.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Pieza", "Ruta CAD", "Cantidad", "Dimensiones envolventes mm", "Material/nota", "Uso", "Nivel de fabricacion", "Confianza", "Accion"])
        for item in inventory:
            dims_str = f"{item['dimensions_mm'][0]:.1f}x{item['dimensions_mm'][1]:.1f}x{item['dimensions_mm'][2]:.1f}"
            
            accion = item['fabricacion']
            if accion == "ver_CAD" or accion == "plegar" or accion == "mecanizar":
                accion = f"{accion.capitalize()} con CAD abierto"
            elif "comprar" in accion:
                accion = "Comprar"
            else:
                accion = accion.capitalize()
                
            writer.writerow([item['name'], item['layer_path'], item['count'], dims_str, item['material'], item['uso'], item['fabricacion'], item['confianza'], accion])
            
    with open("cad/inventario.md", "w", encoding="utf-8") as f:
        f.write("# Inventario Operativo\n\n")
        f.write("| Pieza | Ruta CAD | Cantidad | Dimensiones envolventes mm | Material/nota | Uso | Nivel de fabricacion | Confianza | Accion |\n")
        f.write("|---|---|---|---|---|---|---|---|---|\n")
        for item in inventory:
            dims_str = f"{item['dimensions_mm'][0]:.1f}x{item['dimensions_mm'][1]:.1f}x{item['dimensions_mm'][2]:.1f}"
            accion = item['fabricacion']
            if accion == "ver_CAD" or accion == "plegar" or accion == "mecanizar":
                accion = f"{accion.capitalize()} con CAD abierto"
            elif "comprar" in accion:
                accion = "Comprar"
            else:
                accion = accion.capitalize()
            f.write(f"| {item['name']} | {item['layer_path']} | {item['count']} | {dims_str} | {item['material']} | {item['uso']} | {item['fabricacion']} | {item['confianza']} | {accion} |\n")

    print("Extracción completada. Archivos generados en cad/")

if __name__ == "__main__":
    main()
