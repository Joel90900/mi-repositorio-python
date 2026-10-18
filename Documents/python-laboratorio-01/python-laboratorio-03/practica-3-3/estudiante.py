
class Estudiante:
    def __init__(self, nombre, ficha, promedio):
        self.nombre = nombre
        self.ficha = ficha
        self.promedio = promedio

    def mostrar_perfil(self):
        print("Nombre:", self.nombre)
        print("Ficha:", self.ficha)
        print("Promedio:", self.promedio)

    def aprobo(self):
        return self.promedio >= 3.0


ana = Estudiante("Ana", "F123", 2.8)
luis = Estudiante("Luis", "F456", 4.1)

ana.mostrar_perfil()
print("¿Ana aprobó?", ana.aprobo())  

luis.mostrar_perfil()
print("¿Luis aprobó?", luis.aprobo())  