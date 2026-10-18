

def mostrar_productos(productos):
    for producto in productos:
        print(producto)


def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto

    return None


def valor_inventario(productos):
    total = 0

    for producto in productos:
        total += producto["precio"] * producto["cantidad"]

    return total


def productos_sin_stock(productos):
    return [
        producto["nombre"]
        for producto in productos
        if producto["cantidad"] == 0
    ]


inventario = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000, "cantidad": 0},
    {"codigo": "P003", "nombre": "Monitor", "precio": 700000, "cantidad": 2},
]

mostrar_productos(inventario)

encontrado = buscar_producto(inventario, "P002")
print("Búsqueda P002:", encontrado)

print("Valor del inventario:", valor_inventario(inventario))
print("Sin stock:", productos_sin_stock(inventario))