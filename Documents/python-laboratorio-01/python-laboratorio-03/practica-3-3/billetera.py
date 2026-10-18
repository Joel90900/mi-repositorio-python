
class Billetera:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def registrar_ingreso(self, monto):
        if monto <= 0:
            return False

        self.saldo += monto
        return True

    def registrar_gasto(self, monto):
        if monto <= 0:
            return False

        if monto > self.saldo:
            return False

        self.saldo -= monto
        return True

    def consultar_saldo(self):
        return self.saldo


billetera_ana = Billetera("Ana")
billetera_luis = Billetera("Luis")

print("Ingreso Ana 50000:", billetera_ana.registrar_ingreso(50000))
print("Ingreso Ana -100:", billetera_ana.registrar_ingreso(-100))   
print("Gasto Ana 12000:", billetera_ana.registrar_gasto(12000))
print("Gasto Ana 999999:", billetera_ana.registrar_gasto(999999))   
print("Saldo Ana:", billetera_ana.consultar_saldo())

print()

print("Ingreso Luis 30000:", billetera_luis.registrar_ingreso(30000))
print("Gasto Luis 8000:", billetera_luis.registrar_gasto(8000))
print("Saldo Luis:", billetera_luis.consultar_saldo())

print("Saldo final Ana:", billetera_ana.consultar_saldo())
print("Saldo final Luis:", billetera_luis.consultar_saldo())