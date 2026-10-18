

def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal, porcentaje):
    # El porcentaje 10 representa 10 %.
    return subtotal * porcentaje / 100


def calcular_impuesto(base, porcentaje):
    # Calcula el impuesto sobre la base recibida.
    return base * porcentaje / 100


precio = 100000
cantidad = 2
descuento_porcentaje = 10
impuesto_porcentaje = 19

subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal, descuento_porcentaje)
base_descuento = subtotal - descuento
impuesto = calcular_impuesto(base_descuento, impuesto_porcentaje)
total = base_descuento + impuesto

print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Base después del descuento:", base_descuento)
print("Impuesto:", impuesto)
print("Total:", total)