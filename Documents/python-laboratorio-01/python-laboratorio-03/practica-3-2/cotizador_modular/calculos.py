# Reto — Cotizador modular: calculos.py
# Solo contiene los cálculos. Importar este módulo no solicita entradas
# ni ejecuta el cotizador.


def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal, porcentaje):
    return subtotal * porcentaje / 100


def calcular_impuesto(base, porcentaje):
    return base * porcentaje / 100