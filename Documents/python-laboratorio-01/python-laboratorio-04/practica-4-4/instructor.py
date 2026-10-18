# 2. Reutilizar el inicializador con super()
# super().__init__(nombre) llama al constructor de la clase base Empleado.

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre


class Instructor(Empleado):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre)
        self.especialidad = especialidad


instructor = Instructor("Ana", "Python")
print(instructor.nombre)
print(instructor.especialidad)

