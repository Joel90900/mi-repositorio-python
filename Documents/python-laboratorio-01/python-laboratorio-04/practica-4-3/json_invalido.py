# 7. Un JSON puede ser inválido
# Trabaja sobre una COPIA: este script crea productos_copia.json desde
# productos.json y luego le quita una coma para provocar JSONDecodeError.

import json
from pathlib import Path

original = Path("productos.json")
copia = Path("productos_copia.json")

if not original.exists():
    print("Ejecuta primero primer_json.py para crear productos.json.")
else:
    texto = original.read_text(encoding="utf-8")
    # Daño intencional: se elimina la primera coma entre objetos.
    copia.write_text(texto.replace("},", "}", 1), encoding="utf-8")

    try:
        with copia.open("r", encoding="utf-8") as archivo:
            productos = json.load(archivo)
    except json.JSONDecodeError as error:
        print("El archivo no contiene JSON válido.")
        print(f"Detalle: línea {error.lineno}, columna {error.colno}: {error.msg}")
    except FileNotFoundError:
        # La ausencia del archivo es OTRO error distinto.
        print("No se encontró el archivo.")

