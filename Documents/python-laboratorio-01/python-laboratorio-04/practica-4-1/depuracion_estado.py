

class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self._cantidad = cantidad

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_existencias(self, nueva_cantidad):
        if nueva_cantidad < 0:
            raise ValueError("Cantidad inválida.")
        self._cantidad = nueva_cantidad


producto = Producto("Teclado", 4)

try:
    producto.actualizar_existencias(-3)
except ValueError as error:
    print("Rechazado:", error)

print("Cantidad conservada:", producto.cantidad)  

