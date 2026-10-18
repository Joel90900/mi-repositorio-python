

import math

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")


class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        if not isinstance(codigo, str) or codigo.strip() == "":
            raise ValueError("El código no puede estar vacío.")

        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")

        if categoria not in CATEGORIAS:
            mensaje = "Categoría no permitida. Usa: " + ", ".join(CATEGORIAS)
            raise ValueError(mensaje)

        if not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un número.")

        if not math.isfinite(precio):
            raise ValueError("El precio debe ser un número finito.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un número entero.")

        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self._codigo = codigo.strip()
        self._nombre = nombre.strip()
        self._categoria = categoria
        self._precio = float(precio)
        self._cantidad = cantidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_existencias(self, nueva_cantidad):
        """Actualiza la cantidad si es válida. Devuelve True si se actualizó, False en caso contrario."""
        if isinstance(nueva_cantidad, bool) or not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
            return False

        self._cantidad = nueva_cantidad
        return True

    def calcular_valor(self):
        """Calcula el valor total del inventario para este producto (precio * cantidad)."""
        return self._precio * self._cantidad

    def a_diccionario(self):
        """Convierte los datos del objeto en un diccionario serializable a JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Reconstruye una instancia de Producto a partir de un diccionario validando sus campos."""
        if not isinstance(datos, dict):
            raise ValueError("Los datos del producto deben ser un diccionario.")

        campos_esperados = ("codigo", "nombre", "categoria", "precio", "cantidad")
        for campo in campos_esperados:
            if campo not in datos:
                raise ValueError(f"Falta el campo obligatorio '{campo}' en los datos del producto.")

        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["cantidad"],
        )

