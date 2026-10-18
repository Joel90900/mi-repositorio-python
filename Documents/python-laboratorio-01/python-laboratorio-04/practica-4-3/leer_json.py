# 2. Recuperar los datos
# Resultado esperado:
#   P001 - Teclado
#   P002 - Mouse

import json
from pathlib import Path

ruta = Path("productos.json")

with ruta.open("r", encoding="utf-8") as archivo:
    productos = json.load(archivo)

for producto in productos:
    print(producto["codigo"], "-", producto["nombre"])

