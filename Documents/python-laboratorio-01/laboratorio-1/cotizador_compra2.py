
print("=============================")
print("      COTIZADOR PYTHON")
print("=============================")
print()

cliente = input("Nombre del cliente: ")
producto = input("Producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
descuento = int(input("Descuento (%): "))
impuesto = int(input("Impuesto (%): "))

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * (descuento / 100)
base = subtotal - valor_descuento
valor_impuesto = base * (impuesto / 100)
total = base + valor_impuesto

print()
print("-----------------------------")
print("RESUMEN DE COMPRA")
print("-----------------------------")
print(f"Cliente: {cliente}")
print(f"Producto: {producto}")
print(f"Precio unitario: ${precio_unitario}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${valor_descuento}")
print(f"Base: ${base}")
print(f"Impuesto: ${valor_impuesto}")
print(f"TOTAL: ${total}")