# Ejercicio — Catálogo de libros (lectura)
# Modifica a mano un registro de libros.json (por ejemplo el año) y vuelve a
# ejecutar: el programa muestra el valor modificado, porque lee el archivo
# en cada ejecución. Si se rompe el formato, se informa el error.

import json
from pathlib import Path

ruta = Path(__file__).resolve().parent / "libros.json"

try:
    with ruta.open("r", encoding="utf-8") as archivo:
        libros = json.load(archivo)
except FileNotFoundError:
    print("No existe libros.json. Ejecuta primero libros_json.py.")
except json.JSONDecodeError as error:
    print("libros.json no contiene JSON válido:", error)
else:
    for libro in libros:
        print(f"{libro['codigo']} | {libro['titulo']} | "
              f"{libro['autor']} | {libro['anio']}")

