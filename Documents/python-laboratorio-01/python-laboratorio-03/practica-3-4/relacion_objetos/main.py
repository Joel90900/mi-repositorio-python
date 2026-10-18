from producto import Producto
from inventario import Inventario

inventario = Inventario()

inventario.agregar(Producto("P001", "Teclado"))
inventario.agregar(Producto("P002", "Mouse"))

for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)

# Parte 7: búsqueda por código
encontrado = inventario.buscar_por_codigo("P002")

if encontrado is not None:
    print("Encontrado:", encontrado.nombre)
else:
    print("Producto no registrado.")

print()

print("Registrar P001 repetido:", inventario.agregar(Producto("P001", "Teclado")))
print("Eliminar P999 inexistente:", inventario.eliminar("P999"))
print("Eliminar P002 existente:", inventario.eliminar("P002"))
print("Productos en el listado:", len(inventario.listar()))