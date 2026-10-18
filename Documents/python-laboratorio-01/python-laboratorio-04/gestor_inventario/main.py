
import math
from producto import Producto, CATEGORIAS
from inventario import Inventario
from almacenamiento import guardar_inventario, cargar_inventario, RUTA_JSON
from reportes import exportar_csv


def mostrar_menu():
    print()
    print("================================")
    print("       GESTOR DE INVENTARIO     ")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("8. Guardar inventario")
    print("9. Exportar reporte CSV")
    print("0. Salir")


def leer_precio():
    """Solicita un precio numérico finito y mayor que cero con reintentos."""
    while True:
        entrada = input("Precio: ").strip()
        try:
            precio = float(entrada)
        except ValueError:
            print("Debes escribir un número válido.")
            continue

        if not math.isfinite(precio):
            print("El precio debe ser un número finito (no se admite nan o inf).")
            continue

        if precio <= 0:
            print("El precio debe ser mayor que cero.")
            continue

        return precio


def leer_cantidad():
    """Solicita una cantidad entera no negativa con reintentos."""
    while True:
        entrada = input("Cantidad: ").strip()
        try:
            cantidad = int(entrada)
        except ValueError:
            print("Debes escribir un número entero.")
            continue

        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            continue

        return cantidad


def registrar_producto(inventario, persistencia_habilitada):
    codigo = input("Código: ").strip()
    if not codigo:
        print("Registro rechazado: El código no puede estar vacío.")
        return

    if inventario.buscar_por_codigo(codigo) is not None:
        print("Registro rechazado: el código ya existe.")
        return

    nombre = input("Nombre: ").strip()
    if not nombre:
        print("Registro rechazado: El nombre no puede estar vacío.")
        return

    print("Categorías disponibles:", ", ".join(CATEGORIAS))
    categoria = input("Categoría: ").strip()

    try:
        if categoria not in CATEGORIAS:
            print("Registro rechazado: Categoría no permitida. Usa:", ", ".join(CATEGORIAS))
            return

        precio = leer_precio()
        cantidad = leer_cantidad()

        producto = Producto(codigo, nombre, categoria, precio, cantidad)
    except (ValueError, TypeError) as error:
        print("Registro rechazado:", error)
        return

    if inventario.registrar_producto(producto):
        print("Producto registrado.")
        # Auto-guardado seguro
        if persistencia_habilitada:
            try:
                guardar_inventario(inventario)
                print("Inventario guardado.")
            except OSError as err:
                print(f"Advertencia: No se pudo auto-guardar en disco ({err}). El cambio está en memoria.")
    else:
        print("Registro rechazado: el código ya existe.")


def mostrar_producto(producto):
    print(
        f"{producto.codigo} - {producto.nombre} - {producto.categoria} "
        f"- ${producto.precio:.2f} - {producto.cantidad} unidades"
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


def actualizar_existencias(inventario, persistencia_habilitada):
    codigo = input("Código del producto: ").strip()
    if inventario.buscar_por_codigo(codigo) is None:
        print("No se pudo actualizar: producto inexistente.")
        return

    cantidad = leer_cantidad()

    if inventario.actualizar_existencias(codigo, cantidad):
        print("Existencias actualizadas.")
        if persistencia_habilitada:
            try:
                guardar_inventario(inventario)
                print("Inventario guardado.")
            except OSError as err:
                print(f"Advertencia: No se pudo auto-guardar ({err}). Cambio conservado en memoria.")
    else:
        print("No se pudo actualizar existencias.")


def eliminar_producto(inventario, persistencia_habilitada):
    codigo = input("Código del producto: ").strip()

    if inventario.eliminar_producto(codigo):
        print("Producto eliminado.")
        if persistencia_habilitada:
            try:
                guardar_inventario(inventario)
                print("Inventario guardado.")
            except OSError as err:
                print(f"Advertencia: No se pudo auto-guardar ({err}). Cambio conservado en memoria.")
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
    print(f"Valor del inventario: ${valor:.1f}")

    if categorias:
        print("Categorías utilizadas:", len(categorias))
        print("Detalle de categorías:", ", ".join(sorted(categorias)))
    else:
        print("Categorías utilizadas: 0")


def ejecutar_guardado(inventario, persistencia_habilitada):
    if not persistencia_habilitada:
        print("ACCIÓN DENEGADA: El guardado está bloqueado porque el archivo fuente original")
        print("estaba dañado o ilegible al iniciar la sesión. Corrige el archivo para habilitar el guardado.")
        return

    try:
        exito, mensaje = guardar_inventario(inventario)
        print(mensaje)
    except OSError as error:
        print("Error de escritura:", error)


def ejecutar_exportacion_csv(inventario):
    try:
        ruta_csv = exportar_csv(inventario)
        print("Reporte exportado:", ruta_csv)
    except OSError as error:
        print("Error al exportar reporte CSV:", error)


def main():
    inventario, persistencia_habilitada, mensaje_carga = cargar_inventario()
    print(mensaje_carga)

    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            registrar_producto(inventario, persistencia_habilitada)
        elif opcion == "2":
            listar_productos(inventario)
        elif opcion == "3":
            buscar_producto(inventario)
        elif opcion == "4":
            actualizar_existencias(inventario, persistencia_habilitada)
        elif opcion == "5":
            eliminar_producto(inventario, persistencia_habilitada)
        elif opcion == "6":
            productos_sin_stock(inventario)
        elif opcion == "7":
            mostrar_resumen(inventario)
        elif opcion == "8":
            ejecutar_guardado(inventario, persistencia_habilitada)
        elif opcion == "9":
            ejecutar_exportacion_csv(inventario)
        elif opcion == "0":
            # Guardado final de seguridad si está permitido
            if persistencia_habilitada and inventario.listar_productos():
                try:
                    guardar_inventario(inventario)
                except OSError:
                    pass
            print("Programa finalizado.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

