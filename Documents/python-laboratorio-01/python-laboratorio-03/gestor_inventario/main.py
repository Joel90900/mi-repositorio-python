
from producto import Producto, CATEGORIAS
from inventario import Inventario


def mostrar_menu():
    print()
    print("================================")
    print("       GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("0. Salir")


def leer_precio():
    while True:
        try:
            precio = float(input("Precio: "))
        except ValueError:
            print("Debes escribir un número válido.")
            continue

        if precio <= 0:
            print("El precio debe ser mayor que cero.")
            continue

        return precio


def leer_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Debes escribir un número entero.")
            continue

        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            continue

        return cantidad


def registrar_producto(inventario):
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    print("Categorías disponibles:", ", ".join(CATEGORIAS))
    categoria = input("Categoría: ").strip()
    precio = leer_precio()
    cantidad = leer_cantidad()

    try:
        producto = Producto(codigo, nombre, categoria, precio, cantidad)
    except ValueError as error:
        print("Registro rechazado:", error)
        return

    if inventario.registrar_producto(producto):
        print("Producto registrado.")
    else:
        print("Registro rechazado: el código ya existe.")


def mostrar_producto(producto):
    print(
        f"{producto.codigo} - {producto.nombre} - {producto.categoria} "
        f"- ${producto.precio} - {producto.cantidad} unidades"
    )


def listar_productos(inventario):
    productos = inventario.listar_productos()

    if not productos:
        print("El inventario está vacío.")
        return

    for producto in productos:
        mostrar_producto(producto)


def buscar_producto(inventario):
    codigo = input("Código a buscar: ").strip()
    producto = inventario.buscar_por_codigo(codigo)

    if producto is None:
        print("Producto no registrado.")
    else:
        mostrar_producto(producto)


def actualizar_existencias(inventario):
    codigo = input("Código del producto: ").strip()
    cantidad = leer_cantidad()

    if inventario.actualizar_existencias(codigo, cantidad):
        print("Existencias actualizadas.")
    else:
        print("No se pudo actualizar: producto inexistente.")


def eliminar_producto(inventario):
    codigo = input("Código del producto: ").strip()

    if inventario.eliminar_producto(codigo):
        print("Producto eliminado.")
    else:
        print("Producto no registrado.")


def productos_sin_stock(inventario):
    agotados = inventario.productos_sin_stock()

    if not agotados:
        print("No hay productos sin existencias.")
    else:
        print("Sin existencias:")
        for nombre in agotados:
            print("-", nombre)


def mostrar_resumen(inventario):
    cantidad, unidades, valor, categorias = inventario.resumen()

    print("Productos registrados:", cantidad)
    print("Unidades disponibles:", unidades)
    print("Valor del inventario: $", valor, sep="")

    if categorias:
        print("Categorías utilizadas:", ", ".join(sorted(categorias)))
    else:
        print("Categorías utilizadas: Ninguna")


def main():
    inventario = Inventario()
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            registrar_producto(inventario)
        elif opcion == "2":
            listar_productos(inventario)
        elif opcion == "3":
            buscar_producto(inventario)
        elif opcion == "4":
            actualizar_existencias(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            productos_sin_stock(inventario)
        elif opcion == "7":
            mostrar_resumen(inventario)
        elif opcion == "0":
            print("Programa finalizado.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()