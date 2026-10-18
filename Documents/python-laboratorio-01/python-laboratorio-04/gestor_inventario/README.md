# Gestor de Inventario Persistente (Laboratorio 4)

Aplicación de consola en Python para la administración de inventario con persistencia en formato JSON, exportación de reportes tabulares a CSV, y arquitectura modular bajo principios de Programación Orientada a Objetos (POO).

---

## 1. Distribución de Responsabilidades y Arquitectura

El proyecto está diseñado bajo el principio de **Separación de Responsabilidades (SoC)**:

| Módulo / Archivo | Responsabilidad Principal | ¿Conoce el Sistema de Archivos? | ¿Usa `input()` / `print()`? |
| :--- | :--- | :---: | :---: |
| `producto.py` | Modela la entidad `Producto`. Valida en tiempo de creación tipos, valores finitos, precios positivos y cantidades enteras. Serializa a diccionario (`a_diccionario`) y deserializa con validación (`desde_diccionario`). | No | No |
| `inventario.py` | Administra la colección interna en memoria de objetos `Producto`. Garantiza unicidad de códigos, cálculo de resúmenes y carga atómica (`desde_lista_datos`). | No | No |
| `almacenamiento.py` | Persistencia en disco (`datos/productos.json`) mediante rutas absolutas `pathlib.Path`. Maneja los 3 estados de archivo: inexistente, válido y dañado (sin sobrescritura destructiva). Utiliza guardado atómico y copias `.bak`. | Sí | No |
| `reportes.py` | Genera reportes en formato CSV (`reportes/inventario.csv`) con UTF-8 y cálculo de valor monetario total de existencias (`precio * cantidad`). | Sí | No |
| `main.py` | Única capa de interacción con el usuario (interfaz de consola). Valida entradas, reintenta ante errores y orquesta las operaciones del inventario. | Indirectamente | Sí |

---

## 2. Requisitos y Ejecución

- **Python 3.10+** (probado y verificado en Python 3.14)
- No requiere dependencias externas (utiliza únicamente módulos de la biblioteca estándar: `pathlib`, `json`, `csv`, `math`).

Para ejecutar el programa:

```bash
cd gestor_inventario
python main.py
```

---

## 3. Menú de Opciones

```text
================================
       GESTOR DE INVENTARIO     
================================
1. Registrar producto
2. Listar productos
3. Buscar por código
4. Actualizar existencias
5. Eliminar producto
6. Consultar productos sin stock
7. Resumen del inventario
8. Guardar inventario
9. Exportar reporte CSV
0. Salir
```

---

## 4. Pruebas Obligatorias y Validación Numérica

### Prueba Numérica de Referencia:
1. Registro de productos:
   - `P001` - Teclado ($85,000, 4 unidades, Periféricos)
   - `P002` - Mouse ($45,000, 0 unidades, Periféricos)
   - `P003` - Monitor ($700,000, 2 unidades, Componentes)
2. Resumen esperado:
   - Productos registrados: 3
   - Unidades disponibles: 6
   - Valor total: $1,740,000.0
   - Sin existencias: Mouse
   - Categorías utilizadas: 2 (Componentes, Periféricos)
3. Modificación y persistencia:
   - Se actualiza existencias de Mouse a 5 unidades.
   - Resumen posterior: 11 unidades, Valor total: $1,965,000.0.
   - En el reporte CSV, el valor del inventario para `P002` es exactamente `$225,000.00` ($45,000 * 5).

---

## 5. Tratamiento de Archivos Dañados (Protección de Integridad)

Si `productos.json` contiene un error de sintaxis (por ejemplo, una coma eliminada o corchetes corruptos):
1. `almacenamiento.py` captura `json.JSONDecodeError` e informa la línea y columna del error.
2. La bandera de persistencia se desactiva: **el programa bloquea la sobrescritura del archivo**.
3. Se evita que una lista vacía `[]` destruya la información original susceptible de recuperación manual.

