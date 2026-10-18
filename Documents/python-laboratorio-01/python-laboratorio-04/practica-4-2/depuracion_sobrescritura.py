# Depuración — Sobrescritura accidental
#
# Versión original (con error):
#
#   ruta = Path("historial.txt")
#   ruta.write_text("Registro 1\n", encoding="utf-8")
#   ruta.write_text("Registro 2\n", encoding="utf-8")
#
# ¿Por qué solo queda el segundo registro? write_text() abre el archivo en
# modo escritura ("w"): cada llamada reemplaza todo el contenido anterior.
#
# Corrección A: escribir el primero y AGREGAR el segundo con modo "a".
# Corrección B: escribir ambas líneas en una sola operación.

from pathlib import Path

ruta = Path("historial.txt")

# Corrección A
ruta.write_text("Registro 1\n", encoding="utf-8")
with open(ruta, "a", encoding="utf-8") as archivo:
    archivo.write("Registro 2\n")
print("Corrección A:")
print(ruta.read_text(encoding="utf-8"))

# Corrección B
ruta.write_text("Registro 1\nRegistro 2\n", encoding="utf-8")
print("Corrección B:")
print(ruta.read_text(encoding="utf-8"))

