

from producto import Producto


class Inventario:
    def __init__(self):
        self._productos = []

    def registrar_producto(self, producto):
        """Registra un producto si no existe otro con el mismo código."""
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden registrar instancias de la clase Producto.")

        if self.buscar_por_codigo(producto.codigo) is not None:
            return False

        self._productos.append(producto)
        return True

    def listar_productos(self):
        """Devuelve una copia superficial de la lista para proteger la interna."""
        return self._productos.copy()

    def buscar_por_codigo(self, codigo):
        """Busca un producto por su código y lo devuelve, o None si no existe."""
        if not codigo:
            return None
        codigo_limpio = codigo.strip()
        for producto in self._productos:
            if producto.codigo == codigo_limpio:
                return producto
        return None

    def actualizar_existencias(self, codigo, nueva_cantidad):
        """Actualiza las existencias de un producto según las reglas de negocio."""
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False

        return producto.actualizar_existencias(nueva_cantidad)

    def eliminar_producto(self, codigo):
        """Elimina un producto por su código. Devuelve True si se eliminó, False si no existía."""
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False

        self._productos.remove(producto)
        return True

    def productos_sin_stock(self):
        """Devuelve la lista de nombres de productos que tienen cantidad 0."""
        return [producto.nombre for producto in self._productos if producto.cantidad == 0]

    def resumen(self):
        """Devuelve una tupla (cantidad_productos, total_unidades, valor_total, categorias)."""
        cantidad = len(self._productos)
        unidades = sum(producto.cantidad for producto in self._productos)
        valor = sum(producto.calcular_valor() for producto in self._productos)
        categorias = {producto.categoria for producto in self._productos}
        return cantidad, unidades, valor, categorias

    def exportar_datos(self):
        """Devuelve una lista de diccionarios con los datos de todos los productos."""
        return [producto.a_diccionario() for producto in self._productos]

    @classmethod
    def desde_lista_datos(cls, lista_datos):
        """
        Construye una nueva instancia de Inventario a partir de una lista de diccionarios.
        Aplica validación atómica: si algún producto falla o hay códigos duplicados,
        se lanza una excepción y no se crea un inventario corrupto.
        """
        if not isinstance(lista_datos, list):
            raise ValueError("Los datos del inventario deben ser una lista de registros.")

        nuevo_inventario = cls()
        codigos_vistos = set()

        for indice, item in enumerate(lista_datos, start=1):
            if not isinstance(item, dict):
                raise ValueError(f"El registro #{indice} no es un diccionario válido.")

            # Reconstrucción aplicando validaciones del constructor de Producto
            producto = Producto.desde_diccionario(item)

            if producto.codigo in codigos_vistos:
                raise ValueError(f"Código duplicado detectado en los datos: '{producto.codigo}'.")

            codigos_vistos.add(producto.codigo)
            nuevo_inventario.registrar_producto(producto)

        return nuevo_inventario

