

import json
import shutil
from pathlib import Path
from inventario import Inventario

BASE_DIR = Path(__file__).resolve().parent
CARPETA_DATOS = BASE_DIR / "datos"
RUTA_JSON = CARPETA_DATOS / "productos.json"
RUTA_BACKUP = CARPETA_DATOS / "productos.json.bak"


def guardar_inventario(inventario, ruta=RUTA_JSON):
    """
    Obtiene los datos mediante inventario.exportar_datos().
    Crea el directorio si no existe.
    Escribe mediante archivo temporal y reemplazo atómico para evitar corrupción por apagón/corte.
    Crea copia de seguridad previa si el archivo original existe.
    Devuelve (True, "Mensaje de éxito") o lanza OSError/IOError con detalle.
    """
    try:
        CARPETA_DATOS.mkdir(parents=True, exist_ok=True)
        datos = inventario.exportar_datos()

        if ruta.exists():
            try:
                shutil.copy2(ruta, RUTA_BACKUP)
            except OSError:
                pass 

        ruta_temporal = ruta.with_suffix(".tmp")
        with ruta_temporal.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)

        ruta_temporal.replace(ruta)
        return True, f"Inventario guardado exitosamente en: {ruta.name}"

    except (OSError, TypeError, ValueError) as error:
        ruta_temp = ruta.with_suffix(".tmp")
        if ruta_temp.exists():
            try:
                ruta_temp.unlink()
            except OSError:
                pass
        raise OSError(f"Error al escribir en el archivo '{ruta}': {error}")


def cargar_inventario(ruta=RUTA_JSON):
    """
    Carga el inventario desde JSON respetando las 3 situaciones:
    1. Archivo inexistente -> Devuelve (Inventario vacío, True, "Nuevo inventario inicializado").
    2. Archivo válido -> Reconstruye y valida productos. Devuelve (Inventario cargado, True, "...").
    3. Archivo existente pero dañado o con datos inválidos ->
       Devuelve (Inventario vacío, False, "Descripción del problema").
       El indicador booleano 'True/False' determina si es seguro operar y guardar.
    """
    if not ruta.exists():
        return Inventario(), True, "Archivo de datos no encontrado. Se inició con inventario nuevo y vacío."

    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except json.JSONDecodeError as error:
        mensaje = (
            f"ERROR CRÍTICO: El archivo '{ruta.name}' tiene un error de formato JSON "
            f"(línea {error.lineno}, columna {error.colno}: {error.msg}).\n"
            f"Para proteger los datos existentes, el guardado automático ha sido DESHABILITADO."
        )
        return Inventario(), False, mensaje
    except OSError as error:
        mensaje = f"ERROR: No se pudo leer el archivo '{ruta.name}': {error}"
        return Inventario(), False, mensaje

    try:
        inventario = Inventario.desde_lista_datos(datos)
        return inventario, True, f"Se cargaron correctamente {len(inventario.listar_productos())} productos."
    except (ValueError, TypeError) as error:
        mensaje = (
            f"ERROR DE INTEGRIDAD: Los datos dentro de '{ruta.name}' no son válidos: {error}\n"
            f"El archivo existente NO ha sido modificado ni sobrescrito."
        )
        return Inventario(), False, mensaje

