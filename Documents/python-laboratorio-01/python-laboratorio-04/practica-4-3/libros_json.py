# Ejercicio — Catálogo de libros (escritura)
# Guarda tres libros en libros.json. Para leerlos ejecuta leer_libros.py.

import json
from pathlib import Path

libros = [
    {"codigo": "L001", "titulo": "Cien años de soledad",
     "autor": "Gabriel García Márquez", "anio": 1967},
    {"codigo": "L002", "titulo": "La vorágine",
     "autor": "José Eustasio Rivera", "anio": 1924},
    {"codigo": "L003", "titulo": "María",
     "autor": "Jorge Isaacs", "anio": 1867},
]

ruta = Path(__file__).resolve().parent / "libros.json"

with ruta.open("w", encoding="utf-8") as archivo:
    json.dump(libros, archivo, ensure_ascii=False, indent=4)

print("Libros guardados en", ruta)

