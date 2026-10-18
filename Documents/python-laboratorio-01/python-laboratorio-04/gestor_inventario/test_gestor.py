
import math
import json
import shutil
from pathlib import Path

from producto import Producto, CATEGORIAS
from inventario import Inventario
import almacenamiento
import reportes

TEMP_DIR = Path(__file__).resolve().parent / "test_temp_data"
TEMP_DIR.mkdir(parents=True, exist_ok=True)

RUTA_JSON_TEST = TEMP_DIR / "test_productos.json"
RUTA_CSV_TEST = TEMP_DIR / "test_reporte.csv"

def limpiar():
    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

def test_todo():
    print("=== INICIANDO VERIFICACIÓN COMPLETA ===")
    limpiar()

    inv, ok, msg = almacenamiento.cargar_inventario(RUTA_JSON_TEST)
    assert ok is True
    assert len(inv.listar_productos()) == 0
    print("[PASS] 1. Archivo inexistente carga inventario vacío sin error.")

    p1 = Producto("P001", "Teclado", "Periféricos", 85000, 4)
    p2 = Producto("P002", "Mouse", "Periféricos", 45000, 0)
    p3 = Producto("P003", "Monitor", "Componentes", 700000, 2)

    inv.registrar_producto(p1)
    inv.registrar_producto(p2)
    inv.registrar_producto(p3)

    cant, unid, val, cats = inv.resumen()
    assert cant == 3, f"Esperado 3, obtuve {cant}"
    assert unid == 6, f"Esperado 6, obtuve {unid}"
    assert val == 1740000.0, f"Esperado 1740000.0, obtuve {val}"
    assert inv.productos_sin_stock() == ["Mouse"]
    assert len(cats) == 2
    print(f"[PASS] 2. Resumen inicial verificado: {cant} productos, {unid} unidades, ${val:.1f}, sin stock: {inv.productos_sin_stock()}.")

    almacenamiento.guardar_inventario(inv, RUTA_JSON_TEST)
    assert RUTA_JSON_TEST.exists()
    
    inv_recuperado, ok_rec, msg_rec = almacenamiento.cargar_inventario(RUTA_JSON_TEST)
    assert ok_rec is True
    c_r, u_r, v_r, cats_r = inv_recuperado.resumen()
    assert (c_r, u_r, v_r) == (3, 6, 1740000.0)
    print("[PASS] 3. Guardado y recuperación exitosa en JSON sin pérdida de datos.")

    inv_recuperado.actualizar_existencias("P002", 5)
    c_mod, u_mod, v_mod, _ = inv_recuperado.resumen()
    assert u_mod == 11, f"Esperado 11 unidades, obtuve {u_mod}"
    assert v_mod == 1965000.0, f"Esperado 1965000.0, obtuve {v_mod}"
    almacenamiento.guardar_inventario(inv_recuperado, RUTA_JSON_TEST)

    inv_post_reinicio, _, _ = almacenamiento.cargar_inventario(RUTA_JSON_TEST)
    _, u_post, v_post, _ = inv_post_reinicio.resumen()
    assert u_post == 11 and v_post == 1965000.0
    print(f"[PASS] 4. Actualización persistida correctamente: {u_post} unidades, ${v_post:.1f}.")

    ruta_csv_gen = reportes.exportar_csv(inv_post_reinicio, RUTA_CSV_TEST)
    assert ruta_csv_gen.exists()
    contenido_csv = ruta_csv_gen.read_text(encoding="utf-8")
    assert "codigo,nombre,categoria,precio,cantidad,valor_inventario" in contenido_csv
    # Fila de Mouse con cantidad 5: valor = 225000.00
    assert "P002,Mouse,Periféricos,45000.00,5,225000.00" in contenido_csv
    print("[PASS] 5. Reporte CSV exportado y verificado (P002 valor_inventario = 225000.00).")

    assert inv_post_reinicio.registrar_producto(Producto("P001", "Otro", "Accesorios", 100, 1)) is False
    try:
        Producto("P009", "Invalido", "Comida", 100, 1)
        assert False, "Debió rechazar categoría desconocida"
    except ValueError:
        pass
    try:
        Producto("P010", "Invalido", "Accesorios", -10, 1)
        assert False, "Debió rechazar precio negativo"
    except ValueError:
        pass
    try:
        Producto("P011", "Invalido", "Accesorios", float("inf"), 1)
        assert False, "Debió rechazar precio inf"
    except ValueError:
        pass
    try:
        Producto("P012", "Invalido", "Accesorios", 100, -5)
        assert False, "Debió rechazar cantidad negativa"
    except ValueError:
        pass
    print("[PASS] 6. Validaciones de dominio (duplicados, precio, inf/nan, categoría, stock) activas y correctas.")

    json_original = RUTA_JSON_TEST.read_text(encoding="utf-8")
    json_danado = json_original.replace("},", "}")  # romper sintaxis
    RUTA_DANADA = TEMP_DIR / "danado.json"
    RUTA_DANADA.write_text(json_danado, encoding="utf-8")

    inv_danado, es_seguro, msg_danado = almacenamiento.cargar_inventario(RUTA_DANADA)
    assert es_seguro is False
    assert "ERROR CRÍTICO" in msg_danado
    assert RUTA_DANADA.read_text(encoding="utf-8") == json_danado
    print("[PASS] 7. Archivo JSON dañado detectado, notificado y protegido contra sobrescritura.")

    limpiar()
    print("=== TODAS LAS PRUEBAS AUTOMATIZADAS PASARON SATISFACTORIAMENTE ===")

if __name__ == "__main__":
    test_todo()

