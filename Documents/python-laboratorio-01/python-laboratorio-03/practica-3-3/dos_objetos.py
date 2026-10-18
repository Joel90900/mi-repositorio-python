class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_detalle(self):
        print("Código:", self.codigo)
        print("Producto:", self.nombre)
        print("Precio:", self.precio)
        print("Cantidad:", self.cantidad)

    def calcular_valor(self):
        return self.precio * self.cantidad


teclado = Producto("P001", "Teclado", 85000, 4)
mouse = Producto("P002", "Mouse", 45000, 7)

print("Valor del teclado:", teclado.calcular_valor())
print("Valor del mouse:", mouse.calcular_valor())

mouse.cantidad = 2

print("Cantidad del teclado:", teclado.cantidad)
print("Cantidad del mouse:", mouse.cantidad)