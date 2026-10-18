

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)


primero = Inventario()
segundo = Inventario()

primero.agregar("Teclado")
print(segundo.productos)  