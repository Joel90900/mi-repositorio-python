

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(self.nombre)


persona = Persona("Laura")
persona.mostrar()

persona = Persona("Luis")
persona.mostrar()