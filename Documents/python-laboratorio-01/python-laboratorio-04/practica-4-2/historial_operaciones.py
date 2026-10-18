
import math
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_HISTORIAL = BASE_DIR / "operaciones.txt"
SEPARADOR = ";"


def mostrar_menu():
    print()
    print("1. Registrar operación")
    print("2. Mostrar historial")
    print("0. Salir")


def leer_valor():
    while True:
        try:
            valor = float(input("Valor: "))
        except ValueError:
            print("Debes escribir un número.")
            continue

        if not math.isfinite(valor):
            print("El valor debe ser un número finito.")
            continue

        return valor


def registrar_operacion():
    concepto = input("Concepto: ").strip()
    if concepto == "":
        print("El concepto no puede estar vacío.")
        return

    concepto = concepto.replace(SEPARADOR, ",")
    valor = leer_valor()

    try:
        with open(RUTA_HISTORIAL, "a", encoding="utf-8") as archivo:
            archivo.write(f"{concepto}{SEPARADOR}{valor}\n")
    except OSError as error:
        print("No se pudo guardar la operación:", error)
        return

    print("Operación registrada.")


def mostrar_historial():
    try:
        with open(RUTA_HISTORIAL, "r", encoding="utf-8") as archivo:
            lineas = [linea.strip() for linea in archivo if linea.strip()]
    except FileNotFoundError:
        print("Todavía no hay operaciones registradas.")
        return

    if not lineas:
        print("El historial está vacío.")
        return

    for numero, linea in enumerate(lineas, start=1):
        concepto, _, valor = linea.rpartition(SEPARADOR)
        print(f"{numero}. {concepto} -> {valor}")


def main():
    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            registrar_operacion()
        elif opcion == "2":
            mostrar_historial()
        elif opcion == "0":
            print("Programa finalizado.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

