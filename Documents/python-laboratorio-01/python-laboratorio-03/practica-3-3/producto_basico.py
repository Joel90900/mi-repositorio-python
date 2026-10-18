class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad


teclado = Producto("P001", "Teclado", 85000, 4)

print(teclado.codigo)
print(teclado.nombre)
print(teclado.precio)
print(teclado.cantidad)