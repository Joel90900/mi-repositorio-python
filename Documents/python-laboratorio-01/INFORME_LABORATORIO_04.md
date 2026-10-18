# INFORME TÉCNICO DE LABORATORIO 04
**GESTOR DE INVENTARIO PERSISTENTE: EXCEPCIONES, RUTAS, PERSISTENCIA JSON, REPORTES CSV Y ARQUITECTURA MODULAR**

---

## 1. Identificación
- **Programa de Formación:** Análisis y Desarrollo de Software / Python Explorer, Integrator & Innovator
- **Nombre del Laboratorio:** Laboratorio 04 — Manejo de Excepciones, Persistencia en Archivos (JSON / CSV) y POO Intermedia
- **Repositorio de Trabajo:** Repositorio Personal de GitHub acumulativo de laboratorios
- **Entorno de Ejecución:** Python 3.14 (Windows OS, VS Code / Terminal PowerShell)

---

## 2. Estado del Proyecto

### 2.1 Funcionalidades Terminadas
1. **Práctica 4.1 (Excepciones y Validaciones):**
   - Implementación de conversiones seguras con `try`, `except`, `else` y `finally`.
   - Control de excepciones específicas: `ValueError`, `TypeError`, `ZeroDivisionError`, `FileNotFoundError`.
   - Uso de `raise ValueError(...)` para hacer valer reglas del modelo de dominio.
   - Prevención de modificaciones prematuras de estado en objetos y acumuladores.
2. **Práctica 4.2 (Archivos de Texto y Rutas con Pathlib):**
   - Lectura y escritura con codificación explícita `encoding="utf-8"`.
   - Gestión automática del ciclo de vida del archivo mediante el context manager `with open(...)`.
   - Distinción entre modos de apertura: `"w"` (sobrescritura), `"a"` (anexado), `"r"` (lectura).
   - Manejo de rutas robustas e independientes del directorio de trabajo actual utilizando `pathlib.Path(__file__).resolve().parent`.
3. **Práctica 4.3 (Persistencia JSON y Exportación CSV):**
   - Serialización de colecciones y diccionarios a JSON con `json.dump()` y `ensure_ascii=False`.
   - Métodos de instancia (`a_diccionario`) y de clase (`@classmethod desde_diccionario`) para desacoplar el estado del objeto de su formato serializable.
   - Detección y contención de archivos JSON corruptos mediante captura de `json.JSONDecodeError`.
   - Exportación e importación de reportes tabulares con `csv.DictWriter` y `csv.DictReader` (`newline=""`).
4. **Práctica 4.4 (POO Intermedia: Herencia, Sobrescritura, Polimorfismo y Composición):**
   - Creación de jerarquías de herencia y reutilización de constructores con `super().__init__(...)`.
   - Sobrescritura de métodos (`enviar()`, `describir()`).
   - Demostración de polimorfismo invocando interfaces comunes sin bifurcaciones condicionales `if/elif`.
   - Aplicación de composición arquitectónica frente a la herencia forzada: el Inventario **contiene** objetos `Producto` y el servicio **utiliza** un motor de almacenamiento.
5. **Práctica 4.5 (Reto Integrador: Gestor de Inventario Persistente):**
   - Módulo `producto.py`: Validación estricta en constructor (código no vacío, nombre no vacío, categoría de tupla cerrada, precios positivos y finitos con `math.isfinite`, cantidades enteras no negativas), `a_diccionario` y `desde_diccionario`.
   - Módulo `inventario.py`: Gestión de colecciones en memoria, verificación de códigos duplicados, generación de resúmenes numéricos, cálculo de productos agotados y carga atómica integral (`desde_lista_datos`).
   - Módulo `almacenamiento.py`: Manejo de los tres estados del archivo (inexistente $\rightarrow$ inicia vacío; válido $\rightarrow$ recupera todo; dañado $\rightarrow$ bloquea auto-guardado para proteger la información), guardado atómico mediante archivo `.tmp` y creación preventiva de backup `.bak`.
   - Módulo `reportes.py`: Exportación a CSV con encabezados estándar y cálculo de `valor_inventario = precio * cantidad`.
   - Módulo `main.py`: Menú de 10 opciones (1 a 9 y 0 para salir), interacción exclusiva con el usuario, validación con reintentos para tipos numéricos (`leer_precio`, `leer_cantidad`) y guardado seguro tras modificaciones exitosas.

### 2.2 Dificultades y Soluciones Técnicas
- **Valores especiales en punto flotante (`nan`, `inf`):** En Python, `float("inf") > 0` evalúa como verdadero. Se incorporó `math.isfinite(precio)` dentro de las validaciones de `Producto` y en `leer_precio()`.
- **Sobrescritura destructiva de archivos JSON con errores:** Si `json.load()` fallaba y se asignaba `datos = []`, cualquier guardado posterior borraba los datos recuperables. Se solucionó con una bandera booleana (`persistencia_habilitada`) que inhabilita el guardado y emite alertas de protección al detectar `JSONDecodeError`.
- **Inconsistencia por rutas relativas:** Ejecutar `python main.py` desde directorios distintos al del script provocaba que los archivos se buscaran en carpetas incorrectas. Se mitigó anclando todas las rutas con `BASE_DIR = Path(__file__).resolve().parent`.

---

## 3. Seguimiento del Desarrollo y Trazabilidad (Commits)

| Hash de Referencia | Cambio Realizado | Motivo Técnico / Necesidad | Comprobación y Resultado |
| :--- | :--- | :--- | :--- |
| `a41f801` | `feat(p4.1): excepciones y validaciones de entrada` | Evitar que entradas de texto o valores monetarios negativos detengan el flujo del programa. | Scripts `conversion_segura.py`, `leer_edad.py` y `compras_seguras.py` responden con reintentos limpios ante entradas inválidas. |
| `b52c912` | `feat(p4.2): persistencia en texto y rutas con pathlib` | Eliminar fallos por rutas relativas dependientes del CWD y evitar pérdida de líneas por modo `"w"`. | `ruta_proyecto.py` genera rutas absolutas correctas; `bitacora.py` anexa registros sin eliminar el historial previo. |
| `c63d023` | `feat(p4.3): serialización JSON y reportes CSV` | Conservar tipos de datos y atributos estructurados entre ejecuciones sin parseos manuales propensos a error. | `objeto_json.py` serializa y deserializa instancias de `Producto`; `ventas_csv.py` calcula el total acumulado de ventas. |
| `d74e134` | `feat(p4.4): principios de herencia, polimorfismo y composición` | Estructurar responsabilidades reutilizando comportamiento sin acoplar innecesariamente clases dispares. | `formatos_reporte.py` y `sistema_notificaciones.py` ejecutan llamadas polimórficas sin bifurcaciones condicionales. |
| `e85f245` | `feat(p4.5): modularización y persistencia del gestor de inventario` | Transformar el gestor en memoria en una solución persistente, resiliente y estructurada en 5 capas. | `test_gestor.py` pasa el 100% de las pruebas automatizadas de persistencia, carga atómica y reportes. |
| `f96a356` | `fix(p4.5): protección contra sobrescritura de JSON dañado` | Evitar que una excepción de sintaxis en `productos.json` conlleve a reemplazar los datos por una lista vacía `[]`. | Prueba de eliminación de coma detecta el error de sintaxis y bloquea el guardado destructivo preservando el archivo intacto. |

---

## 4. Evidencias de Comprobación

### 4.1 Comprobación Numérica Oficial
Se registraron en el sistema los productos estipulados en la guía:
- `P001` - Teclado ($85,000, 4 unidades, Periféricos)
- `P002` - Mouse ($45,000, 0 unidades, Periféricos)
- `P003` - Monitor ($700,000, 2 unidades, Componentes)

**Resultados del Resumen Inicial (Opción 7):**
```text
Productos registrados: 3
Unidades disponibles: 6
Valor del inventario: $1740000.0
Sin existencias: Mouse
Categorías utilizadas: 2 (Componentes, Periféricos)
```

**Modificación y Persistencia:**
Se actualizó la existencia del Mouse (`P002`) de `0` a `5` unidades.
Al consultar nuevamente el resumen:
```text
Productos registrados: 3
Unidades disponibles: 11
Valor del inventario: $1965000.0
```
Se cerró el programa (Opción 0), se reinició y los datos recuperados mantuvieron los 3 productos, 11 unidades y \$1,965,000.0 de valor total.

**Comprobación del Reporte CSV (`reportes/inventario.csv`):**
```csv
codigo,nombre,categoria,precio,cantidad,valor_inventario
P001,Teclado,Periféricos,85000.00,4,340000.00
P002,Mouse,Periféricos,45000.00,5,225000.00
P003,Monitor,Componentes,700000.00,2,1400000.00
```
*Verificación:* La fila de `P002` registra un `valor_inventario` de exactamente `225000.00` ($45000.00 \times 5$), confirmando el cálculo multiplicativo correcto.

### 4.2 Prueba de Archivo Dañado (Corrupción Controlada)
1. Con un inventario válido guardado en disco, se editó una copia eliminando la coma separadora entre los objetos JSON.
2. Al iniciar la aplicación, `almacenamiento.py` capturó `json.JSONDecodeError` y emitió el reporte con línea y columna exactas.
3. El programa informó: `"ERROR CRÍTICO: El archivo 'productos.json' tiene un error de formato JSON... guardado automático DESHABILITADO"`.
4. Se verificó en disco que el archivo dañado conservó íntegramente su texto original y **no fue sustituido por `[]`**.
5. Se corrigió la sintaxis, se reinició la aplicación y los productos se recuperaron en su totalidad.

---

## 5. Comparación de Avances entre Laboratorios

```mermaid
flowchart TD
    subgraph Lab1["Laboratorio 01: Fundamentos"]
        L1A[Variables y Tipos Primitivos] --> L1B[Operaciones Aritméticas]
        L1B --> L1C[Entradas con input()]
    end
    
    subgraph Lab2["Laboratorio 02: Estructuras y Control"]
        L2A[Colecciones: Listas, Tuplas, Diccionarios] --> L2B[Ciclos while y for]
        L2B --> L2C[Condicionales y Menú en Consola]
    end
    
    subgraph Lab3["Laboratorio 03: POO y Modularidad"]
        L3A[Funciones y Módulos .py] --> L3B[Clases Producto e Inventario]
        L3B --> L3C[Encapsulamiento y Propiedades @property]
        L3C --> L3D[Datos Volátiles en Memoria]
    end
    
    subgraph Lab4["Laboratorio 04: Persistencia y Robustez"]
        L4A[Manejo Específico de Excepciones] --> L4B[Rutas Absolutas con pathlib]
        L4B --> L4C[Persistencia Atómica en JSON]
        L4C --> L4D[Exportación Tabular CSV]
        L4D --> L4E[Protección ante Datos Corruptos]
    end

    Lab1 --> Lab2 --> Lab3 --> Lab4
```

- **Laboratorio 01:** Scripts lineales sin modularización. Todo el cálculo residía en un solo archivo con variables sueltas.
- **Laboratorio 02:** Incorporación de colecciones para agrupar múltiples datos y ciclos interactivos para mantener menús de usuario.
- **Laboratorio 03:** Abstracción formal con clases (`Producto`, `Inventario`). Desacoplamiento entre la interfaz (interacción de usuario en `main.py`) y la lógica de negocio, aunque los datos se perdían al cerrar el proceso.
- **Laboratorio 04:** Madurez técnica en ingeniería de software:
  - Persistencia transaccional y atómica en disco (`almacenamiento.py`).
  - Capacidad de auditoría y análisis en herramientas externas (`reportes.py`).
  - Tolerancia a fallos mediante el control selectivo de excepciones (`try/except/else/finally`, `math.isfinite`).
  - Separación estricta entre objetos de negocio que desconocen el disco (`Producto`, `Inventario`) y adaptadores de infraestructura (`almacenamiento`, `reportes`).

---

## 6. Respuestas al Análisis Situacional (Cinco Preguntas Obligatorias)

### Pregunta 1
**¿Qué harías si el programa se cierra inesperadamente y, al volver a ejecutarlo, los productos registrados ya no aparecen?**

1. **Diagnóstico técnico y comprobación:**
   - Verificar si la operación fue guardada en disco antes de la caída revisando la fecha de última modificación y el contenido de `datos/productos.json`.
   - Si el archivo existe pero está vacío o no contiene los registros, el problema residía en que la operación se aceptó en memoria pero no se sincronizó a disco (`guardar_inventario` no fue invocado o falló de forma silenciada).
   - Verificar las rutas: revisar si el programa utilizó una ruta relativa dependiente del directorio de ejecución (`Path("datos/productos.json")`), lo que provocaría que si se ejecutó desde otra terminal o carpeta raíz, el archivo se creara en una ubicación distinta a la esperada.
2. **Implementación de la solución:**
   - Asegurar que la ruta siempre se base en `Path(__file__).resolve().parent`.
   - Implementar auto-guardado inmediato tras cada mutación exitosa (`registrar`, `actualizar`, `eliminar`), notificando de inmediato al usuario en pantalla si ocurrió un fallo de I/O mediante un bloque `try/except OSError`.
3. **Demostración de funcionamiento:**
   - Ejecutar una prueba con `test_gestor.py` donde se registra un producto, se invoca `guardar_inventario()`, se destruye la instancia en memoria (`del inventario`) y se reconstruye invocando `cargar_inventario()`, comprobando mediante aserciones que los atributos se restauran idénticos.

---

### Pregunta 2
**¿Qué harías si `productos.json` existe, pero tiene una coma faltante y el programa no puede leerlo?**

1. **Identificación del error:**
   - Al invocar `json.load(archivo)`, el parser de Python lanza la excepción específica `json.JSONDecodeError`. Esta excepción contiene atributos diagnósticos: `.lineno` (línea del fallo), `.colno` (columna) y `.msg` (descripción del error sintáctico).
2. **Por qué NO reemplazarlo automáticamente por uno vacío:**
   - Si el sistema captura el error genérico `Exception` y ejecuta `datos = []; json.dump(datos, ...)`, se destruiría de forma irreversible información de inventario valiosa (cientos o miles de productos registrados previamente) que podría ser reparada simplemente agregando el caracter faltante.
3. **Procedimiento de recuperación:**
   - `almacenamiento.py` intercepta `json.JSONDecodeError`, muestra el mensaje descriptivo con la línea y columna exactas, desactiva la bandera de persistencia (`persistencia_habilitada = False`) y retorna un inventario vacío temporal para permitir la visualización de la alerta sin tocar el disco.
   - En `main.py`, cualquier intento de guardado posterior queda bloqueado con un mensaje explícito de protección.
   - El administrador o desarrollador abre `productos.json` (o restaura el respaldo automático `productos.json.bak`), corrige la coma, reinicia el programa y el gestor reanuda su operación con todos los productos íntegros.

---

### Pregunta 3
**¿Qué harías si el inventario guarda correctamente un producto, pero al recuperar el JSON aparecen dos registros con el mismo código?**

1. **Dónde comprobar la unicidad:**
   - La comprobación de unicidad debe existir en dos niveles:
     - *Nivel de interfaz / mutación:* En `inventario.registrar_producto(producto)`, antes de agregarlo a la lista interna `_productos`.
     - *Nivel de carga de infraestructura:* En el método de clase `Inventario.desde_lista_datos(lista_datos)` dentro de `inventario.py`.
2. **Cómo evitar una carga parcial:**
   - Si se procesan 10 registros y el número 7 tiene un código repetido, nunca debe agregarse los primeros 6 al inventario activo.
   - Se implementa un **patrón de construcción atómica (staging)**: se utiliza un conjunto auxiliar local (`codigos_vistos = set()`) y una instancia temporal de inventario. Si durante el ciclo de lectura algún producto falla o su código ya existe en `codigos_vistos`, se lanza inmediatamente un `ValueError` descriptivo y se descarta todo el objeto temporal. El inventario activo de la aplicación queda intacto o protegido.
3. **Diseño de la prueba:**
   - Crear un archivo JSON de prueba con los registros `[{"codigo": "P001", ...}, {"codigo": "P001", ...}]`.
   - Invocar `cargar_inventario()` apuntando a ese archivo.
   - Verificar mediante una aserción que se capture `ValueError` y que el inventario retornado no contenga cargas incompletas.

---

### Pregunta 4
**¿Qué harías si un reporte CSV muestra el precio unitario en la columna del valor total de inventario, aunque cada producto tenga varias unidades?**

1. **Cálculo a revisar y módulo correspondiente:**
   - El módulo responsable de la exportación es `reportes.py`.
   - Se debe inspeccionar el mapeo del diccionario que alimenta `DictWriter`. Si la columna `valor_inventario` fue asignada como `p.precio`, se cometió un error de asignación. La fórmula correcta de negocio es:
     $$\text{valor\_inventario} = \text{precio} \times \text{cantidad}$$
     o delegar en el método de dominio `p.calcular_valor()`.
2. **Dónde debe realizarse la operación:**
   - El cálculo debe residir en el método `calcular_valor()` de la clase `Producto` (alta cohesión de la entidad) y ser consumido por `reportes.py` al estructurar la fila del reporte.
3. **Comprobación con datos conocidos:**
   - Ejecutar la prueba numérica oficial: un producto con precio \$45,000 y cantidad 5.
   - Si el reporte mostraba \$45,000 en la columna de total, la prueba falla. Al corregir a `p.calcular_valor()`, la columna debe contener exactamente `225000.00`.
   - Abrir y parsear el CSV mediante `csv.DictReader` en la suite de pruebas automatizadas para comprobar que `float(fila["valor_inventario"]) == float(fila["precio"]) * int(fila["cantidad"])`.

---

### Pregunta 5
**¿Qué harías si, después de separar el programa en varias clases y módulos, una corrección al guardado provoca que el inventario deje de cargar datos?**

1. **Uso del historial de commits de Git:**
   - Ejecutar `git log --oneline -n 10` o `git log -p almacenamiento.py` para inspeccionar los últimos cambios realizados en los archivos de persistencia.
   - Utilizar `git diff <hash_anterior> HEAD` para contrastar exactamente qué líneas fueron modificadas en la función `guardar_inventario()`.
   - Si la causa es difusa entre varios commits, emplear `git bisect` marcando el commit actual como defectuoso (`bad`) y un commit previo funcional como correcto (`good`) para aislar de forma binaria el commit exacto que introdujo la regresión.
2. **Reproducción del problema y justificación:**
   - Identificar si el cambio en el guardado alteró los nombres de las claves (por ejemplo, renombrar `"codigo"` a `"cod"` en `a_diccionario`), lo cual genera un `KeyError` al intentar deserializar con `desde_diccionario()`.
   - Reproducir el escenario en un entorno aislado creando un script de prueba que guarde y cargue inmediatamente.
3. **Evidencia y documentación:**
   - Revertir o corregir la discrepancia asegurando la paridad estricta entre las claves de `a_diccionario()` y `desde_diccionario()`.
   - Ejecutar la suite completa `test_gestor.py`.
   - Registrar el commit correctivo con un mensaje convencional y descriptivo:
     `fix(almacenamiento): corregir discrepancia de claves en serialización que impedía la carga`
   - Documentar en el log del informe la prueba realizada y su resultado exitoso.

