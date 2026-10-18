

import json

mal_formado = """[
    {"codigo": "P001", "nombre": "Teclado"}
    {"codigo": "P002", "nombre": "Mouse"}
]"""

corregido = """[
    {"codigo": "P001", "nombre": "Teclado"},
    {"codigo": "P002", "nombre": "Mouse"}
]"""

try:
    json.loads(mal_formado)
except json.JSONDecodeError as error:
    print("Mal formado ->", error)

productos = json.loads(corregido)
print("Corregido ->", productos)

