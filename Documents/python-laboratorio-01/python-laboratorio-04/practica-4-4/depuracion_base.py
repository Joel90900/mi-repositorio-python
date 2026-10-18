# Depuración — No se inicializó la clase base
#
# Error original:
#   class Persona:
#       def __init__(self, nombre):
#           self.nombre = nombre
#   class Aprendiz(Persona):
#       def __init__(self, nombre, ficha):
#           self.ficha = ficha
#   aprendiz = Aprendiz("Carlos", "123456")
#   print(aprendiz.nombre)  # AttributeError: 'Aprendiz' object has no attribute 'nombre'
#
# ¿Por qué falla? Al sobrescribir __init__ en Aprendiz sin invocar super().__init__(nombre),
# el atributo self.nombre nunca llega a inicializarse en la instancia.
#
# Corrección:

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Aprendiz(Persona):
    def __init__(self, nombre, ficha):
        super().__init__(nombre)  # Inicializa la clase base Persona
        self.ficha = ficha


aprendiz = Aprendiz("Carlos", "123456")
print("Nombre:", aprendiz.nombre)
print("Ficha:", aprendiz.ficha)

