import calculos
import validaciones

precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
descuento = float(input("Descuento (%): "))
impuesto = float(input("Impuesto (%): "))

if not (
    validaciones.precio_valido(precio)
    and validaciones.cantidad_valida(cantidad)
    and validaciones.porcentaje_valido(descuento)
    and validaciones.porcentaje_valido(impuesto)
):
    print("Revisa los datos ingresados.")
else:
    subtotal = calculos.calcular_subtotal(precio, cantidad)
    descuento_monto = calculos.calcular_descuento(subtotal, descuento)
    base = subtotal - descuento_monto
    impuesto_monto = calculos.calcular_impuesto(base, impuesto)
    total = base + impuesto_monto

    print("Subtotal:", subtotal)
    print("Descuento:", descuento_monto)
    print("Base después del descuento:", base)
    print("Impuesto:", impuesto_monto)
    print("Total:", total)