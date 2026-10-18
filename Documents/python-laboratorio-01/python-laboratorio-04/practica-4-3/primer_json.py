# 1. ¿Por qué JSON?
# ensure_ascii=False escribe á, é, ñ sin escaparlos; indent=4 facilita la lectura.

import json
from pathlib import Path

productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000, "cantidad": 0},
]

ruta = Path("productos.json")

with ruta.open("w", encoding="utf-8") as archivo:
    json.dump(productos, archivo, ensure_ascii=False, indent=4)

print("Productos guardados.")

