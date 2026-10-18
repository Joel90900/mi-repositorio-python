

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
carpeta = BASE_DIR / "reportes"
carpeta.mkdir(parents=True, exist_ok=True)

ruta = carpeta / "resumen.txt"
lineas = [
    "Reporte de prueba del laboratorio 4",
    "Productos revisados: 3",
    "Estado general: sin novedades",
]
ruta.write_text("\n".join(lineas) + "\n", encoding="utf-8")

print("Contenido del reporte:")
print(ruta.read_text(encoding="utf-8"))
print("Guardado en:", ruta)

