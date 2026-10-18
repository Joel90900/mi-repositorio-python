# Ejercicio — Respetar un archivo dañado
#
# Situación                          Comportamiento
# El archivo no existe               Empezar con lista vacía (y se puede guardar)
# Existe y es válido                 Recuperar los productos
# Existe pero está dañado            Informar y NO sobrescribirlo
#
# Prueba los tres casos:
#   1) borra productos.json y ejecuta;
#   2) ejecuta primer_json.py y luego este script;
#   3) quita una coma de productos.json y ejecuta.

import json
from pathlib import Path

ruta = Path(__file__).resolve().parent / "productos.json"


def cargar_productos():
    """Devuelve (productos, puede_guardar)."""
    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        print("El archivo no existe: se inicia con una lista vacía.")
        return [], True
    except json.JSONDecodeError as error:
        print("ERROR: productos.json tiene un formato inválido.")
        print(f"  línea {error.lineno}, columna {error.colno}: {error.msg}")
        print("  El archivo NO será modificado. Revísalo antes de continuar.")
        return [], False

    if not isinstance(datos, list):
        print("ERROR: se esperaba una lista de productos. No se modificará.")
        return [], False

    return datos, True


productos, puede_guardar = cargar_productos()

print("Productos cargados:", len(productos))
for producto in productos:
    print("-", producto)

if puede_guardar:
    print("Estado: es seguro guardar cambios en el archivo.")
else:
    print("Estado: guardado deshabilitado para proteger el archivo dañado.")
    print("Contenido actual para revisión:")
    print(ruta.read_text(encoding="utf-8"))

