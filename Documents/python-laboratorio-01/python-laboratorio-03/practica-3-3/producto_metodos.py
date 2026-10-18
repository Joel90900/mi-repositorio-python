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
teclado.mostrar_detalle()
print("Valor:", teclado.calcular_valor())