nombre_producto = input("Nombre del producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
porcentaje_descuento = float(input("Porcentaje de descuento: "))

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * porcentaje_descuento / 100
total_despues_descuento = subtotal - valor_descuento

print(f"Producto: {nombre_producto}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Valor del descuento: ${valor_descuento:.2f}")
print(f"Total después del descuento: ${total_despues_descuento:.2f}")
