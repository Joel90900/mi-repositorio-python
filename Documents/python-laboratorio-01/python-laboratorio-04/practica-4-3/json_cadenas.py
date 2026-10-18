# 3. dump, load, dumps y loads
#   json.dump(datos, archivo) -> escribe JSON en un archivo abierto
#   json.load(archivo)        -> lee JSON desde un archivo abierto
#   json.dumps(datos)         -> produce una cadena JSON
#   json.loads(texto)         -> interpreta una cadena JSON

import json

producto = {"nombre": "Cámara", "precio": 120000}

texto = json.dumps(producto, ensure_ascii=False)
recuperado = json.loads(texto)

print(texto)
print(recuperado["nombre"])
print(type(texto), type(recuperado))

