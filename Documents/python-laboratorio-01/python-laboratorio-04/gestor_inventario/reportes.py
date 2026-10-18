# gestor_inventario/reportes.py
# Construye y exporta reportes en formato CSV.
# Columnas requeridas: codigo, nombre, categoria, precio, cantidad, valor_inventario
# Nota: valor_inventario = precio * cantidad (no la suma de precios).

import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CARPETA_REPORTES = BASE_DIR / "reportes"
RUTA_CSV_DEFECTO = CARPETA_REPORTES / "inventario.csv"

CAMPOS_REPORTE = [
    "codigo",
    "nombre",
    "categoria",
    "precio",
    "cantidad",
    "valor_inventario",
]


def exportar_csv(inventario, ruta=RUTA_CSV_DEFECTO):
    """
    Obtiene los datos del inventario a través de su interfaz pública,
    calcula el valor_inventario para cada producto (precio * cantidad)
    y escribe un archivo CSV con encabezados en UTF-8 y newline="".
    Devuelve la ruta absoluta del archivo generado.
    """
    try:
        ruta.parent.mkdir(parents=True, exist_ok=True)

        productos = inventario.listar_productos()
        filas = []

        for p in productos:
            filas.append({
                "codigo": p.codigo,
                "nombre": p.nombre,
                "categoria": p.categoria,
                "precio": f"{p.precio:.2f}",
                "cantidad": p.cantidad,
                "valor_inventario": f"{p.calcular_valor():.2f}",
            })

        with ruta.open("w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_REPORTE)
            escritor.writeheader()
            escritor.writerows(filas)

        return ruta

    except OSError as error:
        raise OSError(f"No se pudo exportar el reporte CSV a '{ruta}': {error}")

