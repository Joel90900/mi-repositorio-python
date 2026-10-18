# Ejercicio — Edad válida
# Pruebas:
#   veinte -> error de conversión
#   -1     -> fuera de rango (negativa)
#   121    -> fuera de rango (superior a 120)
#   20     -> edad aceptada

EDAD_MAXIMA = 120

try:
    edad = int(input("Edad: "))
except ValueError:
    print("Error de conversión: la edad debe ser un número entero.")
else:
    if edad < 0:
        print("Fuera de rango: la edad no puede ser negativa.")
    elif edad > EDAD_MAXIMA:
        print(f"Fuera de rango: la edad no puede superar {EDAD_MAXIMA} años.")
    else:
        print("Edad aceptada:", edad)

