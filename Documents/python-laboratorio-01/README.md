# Repositorio de Aprendizaje: Python Explorer, Integrator & Innovator

Este repositorio contiene la evolución completa y acumulativa de los cuatro laboratorios de desarrollo en Python, demostrando el progreso técnico desde los fundamentos estructurados hasta la persistencia y la arquitectura orientada a objetos modular.

---

## Estructura del Repositorio

```text
python-laboratorio-01/
├── README.md                                  # Guía general de todo el repositorio
├── INFORME_LABORATORIO_04.md                  # Informe técnico detallado de entrega del Lab 04
├── laboratorio-01/ (o raíz)                   # Fundamentos de programación, variables y operaciones
├── laboratorio-02/                            # Colecciones, ciclos y condicionales
├── python-laboratorio-03/                     # Funciones, módulos y POO inicial (Gestor en memoria)
│   ├── practica-3-1/ a practica-3-4/
│   └── gestor_inventario/                     # Gestor del Lab 03 (sin persistencia)
└── python-laboratorio-04/                     # Persistencia, manejo de archivos y POO intermedia
    ├── practica-4-1/                          # Excepciones, validaciones y recuperación de errores
    ├── practica-4-2/                          # Archivos de texto, rutas y pathlib
    ├── practica-4-3/                          # Persistencia con JSON y exportación a CSV
    ├── practica-4-4/                          # Herencia, sobrescritura, polimorfismo y composición
    └── gestor_inventario/                     # Reto Integrador: Gestor de Inventario Persistente
```

---

## Ejecución por Laboratorio

### Laboratorio 03: Gestor de Inventario en Memoria
```bash
cd python-laboratorio-03/gestor_inventario
python main.py
```
*Características:* Modela objetos `Producto` y colección `Inventario`. Los datos se almacenan exclusivamente en memoria volátil y se pierden al salir.

### Laboratorio 04: Gestor de Inventario Persistente (JSON + CSV)
```bash
cd python-laboratorio-04/gestor_inventario
python main.py
```
*Características:* Carga automática al iniciar desde `datos/productos.json`, auto-guardado seguro tras modificaciones, reporte exportable a `reportes/inventario.csv`, protección total ante archivos dañados o con JSON inválido y manejo riguroso de excepciones (`math.isfinite`, tipos de datos, códigos únicos).

Para ejecutar la suite de pruebas automatizadas del Laboratorio 04:
```bash
python python-laboratorio-04/gestor_inventario/test_gestor.py
```

