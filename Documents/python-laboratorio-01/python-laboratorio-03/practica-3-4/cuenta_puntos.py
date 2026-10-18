
class CuentaPuntos:
    def __init__(self, titular):
        self._titular = titular
        self._puntos = 0

    @property
    def titular(self):
        return self._titular

    @property
    def puntos(self):
        return self._puntos

    def sumar(self, cantidad):
        if cantidad <= 0:
            return False

        self._puntos += cantidad
        return True

    def canjear(self, cantidad):
        if cantidad <= 0:
            return False

        if cantidad > self._puntos:
            return False

        self._puntos -= cantidad
        return True


cuenta = CuentaPuntos("Laura")

print("Sumar: 80   ->", cuenta.sumar(80))
print("Canjear: 30 ->", cuenta.canjear(30))
print("Canjear: 100 ->", cuenta.canjear(100))
print("Total:", cuenta.puntos)