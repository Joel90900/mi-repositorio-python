nombre_cliente = input("Ingrese el nombre del cliente: ")
nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad: "))
porcentaje_descuento = int(input("Ingrese el porcentaje de descuento: "))
porcentaje_impuesto = int(input("Ingrese el porcentaje de impuesto: "))

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * porcentaje_descuento / 100
base_despues_descuento = subtotal - valor_descuento
valor_impuesto = base_despues_descuento * porcentaje_impuesto / 100
total_final = base_despues_descuento + valor_impuesto

print("\n--- Cotización de compra ---")
print(f"Cliente: {nombre_cliente}")
print(f"Producto: {nombre_producto}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Valor del descuento: {valor_descuento:.2f}")
print(f"Base después del descuento: {base_despues_descuento:.2f}")
print(f"Valor del impuesto: {valor_impuesto:.2f}")
print(f"Total final: {total_final:.2f}")
0