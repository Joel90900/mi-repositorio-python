
def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


resultado = calcular_subtotal(85000, 3)
print("Subtotal:", resultado)

print()

def mostrar_total(precio, cantidad):
    print(precio * cantidad)


def obtener_total(precio, cantidad):
    return precio * cantidad


mostrar_total(10000, 3)
total = obtener_total(10000, 3)
print("Resultado reutilizable:", total)