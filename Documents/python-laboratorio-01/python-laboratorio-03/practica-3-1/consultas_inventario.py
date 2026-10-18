

inventario = [
    {"nombre": "Teclado", "cantidad": 4},
    {"nombre": "Mouse", "cantidad": 0},
    {"nombre": "Monitor", "cantidad": 0},
    {"nombre": "Cable", "cantidad": 3},
]


def agotados(productos):
    nombres = []

    for producto in productos:
        if producto["cantidad"] == 0:
            nombres.append(producto["nombre"])

    return nombres


print(agotados(inventario))


def agotados_comprension(productos):
    return [
        producto["nombre"]
        for producto in productos
        if producto["cantidad"] == 0
    ]


print(agotados_comprension(inventario))