
class Registro:
    elementos = []


primero = Registro()
segundo = Registro()

primero.elementos.append("Teclado")
print("Segundo (versión con error):", segundo.elementos)

print()

class Registro:
    def __init__(self):
        self.elementos = []


primero = Registro()
segundo = Registro()

primero.elementos.append("Teclado")

print("Primero:", primero.elementos)
print("Segundo:", segundo.elementos)