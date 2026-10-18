# Ejercicio — Vehículos
# Clase Vehiculo con marca y modelo. Motocicleta hereda y agrega cilindraje con super().

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"{self.marca} {self.modelo}"


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje

    def descripcion_completa(self):
        return f"{self.descripcion()} ({self.cilindraje} cc)"


moto1 = Motocicleta("Yamaha", "MT-03", 321)
moto2 = Motocicleta("Honda", "CB500F", 471)

print("Moto 1:", moto1.marca, moto1.modelo, f"{moto1.cilindraje}cc")
print("Detalle 1:", moto1.descripcion_completa())
print("Moto 2:", moto2.marca, moto2.modelo, f"{moto2.cilindraje}cc")
print("Detalle 2:", moto2.descripcion_completa())

