
def calcular_total(precio, cantidad, descuento=0):
    subtotal = precio * cantidad
    return subtotal - subtotal * descuento / 100


print(calcular_total(50000, 2))
print(calcular_total(50000, 2, 10))
print(calcular_total(precio=50000, cantidad=2, descuento=20))