

while True:
    try:
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Debes escribir un entero.")
        continue

    if cantidad < 0:
        print("La cantidad no puede ser negativa.")
        continue

    break

print("Cantidad aceptada:", cantidad)