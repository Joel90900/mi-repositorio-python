# Ejercicio — Exportación de ventas
# Exporta cuatro ventas a ventas.csv, lo vuelve a leer y calcula el total
# vendido convirtiendo la columna "total" a número.

import csv
from pathlib import Path

ruta = Path(__file__).resolve().parent / "ventas.csv"
campos = ["codigo", "producto", "cantidad", "total"]

ventas = [
    {"codigo": "V001", "producto": "Teclado", "cantidad": 2, "total": 170000},
    {"codigo": "V002", "producto": "Mouse", "cantidad": 3, "total": 135000},
    {"codigo": "V003", "producto": "Monitor", "cantidad": 1, "total": 700000},
    {"codigo": "V004", "producto": "Cable HDMI", "cantidad": 5, "total": 75000},
]

with ruta.open("w", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(ventas)

print("Ventas exportadas a", ruta)

total_vendido = 0.0
with ruta.open("r", newline="", encoding="utf-8") as archivo:
    for fila in csv.DictReader(archivo):
        total_vendido += float(fila["total"])  # "170000" -> 170000.0

print("Total vendido:", total_vendido)  # Esperado: 1080000.0

