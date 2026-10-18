# 4, 5 y 6. Los objetos de una clase no se guardan directamente
#
# json.dumps(producto) con una instancia propia produce:
#   TypeError: Object of type Producto is not JSON serializable
# Solución: convertir el objeto a diccionario (a_diccionario) y, para
# recuperarlo, reconstruirlo con un método de clase (desde_diccionario).

import json


class Producto:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        # cls es la clase que recibe la llamada (aquí, Producto).
        return cls(
            datos["codigo"],
            datos["nombre"],
        )


producto = Producto("P001", "Teclado")

# Paso 4: provocar el error controladamente.
try:
    print(json.dumps(producto))
except TypeError as error:
    print("Error esperado:", error)

# Paso 5: convertir a diccionario.
print(json.dumps(producto.a_diccionario(), ensure_ascii=False))

# Paso 6: reconstruir un objeto.
datos = {"codigo": "P002", "nombre": "Mouse"}
nuevo = Producto.desde_diccionario(datos)
print(type(nuevo))
print(nuevo.nombre)

