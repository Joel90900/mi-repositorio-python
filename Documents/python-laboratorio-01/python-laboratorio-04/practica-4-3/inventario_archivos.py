

import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "inventario.json"
RUTA_CSV = BASE_DIR / "inventario.csv"
CAMPOS = ["codigo", "nombre", "precio", "cantidad"]


def cargar():
    """Devuelve (productos, archivo_valido)."""
    try:
        with RUTA_JSON.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        return [], True
    except json.JSONDecodeError as error:
        print(f"inventario.json está dañado ({error.msg}, línea {error.lineno}).")
        return [], False

    if not isinstance(datos, list):
        print("inventario.json no contiene una lista.")
        return [], False

    return datos, True


def guardar(productos):
    with RUTA_JSON.open("w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=4)


def exportar_csv(productos):
    with RUTA_CSV.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(productos)


def leer_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Debes escribir un entero.")
            continue
        if valor < 0:
            print("No se aceptan negativos.")
            continue
        return valor


def main():
    productos, valido = cargar()

    if not valido:
        print("Se detiene el programa para no sobrescribir el archivo dañado.")
        return

    print("Productos recuperados:", len(productos))
    for p in productos:
        print(f"  {p['codigo']} - {p['nombre']} - ${p['precio']} - {p['cantidad']}")

    if input("¿Agregar un producto? (s/n): ").strip().lower() == "s":
        codigo = input("Código: ").strip()
        if any(p["codigo"] == codigo for p in productos):
            print("Código duplicado: no se agrega.")
        else:
            productos.append({
                "codigo": codigo,
                "nombre": input("Nombre: ").strip(),
                "precio": leer_entero("Precio: "),
                "cantidad": leer_entero("Cantidad: "),
            })
            guardar(productos)
            print("Guardado en", RUTA_JSON)

    exportar_csv(productos)
    print("CSV exportado en", RUTA_CSV)


if __name__ == "__main__":
    main()

