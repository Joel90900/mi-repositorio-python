
import math

compras_aceptadas = 0
total = 0.0

print("Registra los importes de compra. Escribe 0 para terminar.")

while True:
    texto = input("Importe: ").strip()

    try:
        importe = float(texto)
    except ValueError:
        print("Entrada rechazada: escribe un número.")
        continue

    if importe == 0:
        break

    if not math.isfinite(importe):
        print("Entrada rechazada: el importe debe ser un número finito.")
        continue

    if importe < 0:
        print("Entrada rechazada: el importe no puede ser negativo.")
        continue

    # Solo se modifica el acumulado cuando el valor fue aceptado.
    compras_aceptadas += 1
    total += importe
    print(f"Compra aceptada. Acumulado: ${total}")

print("Compras aceptadas:", compras_aceptadas)
print(f"Suma acumulada: ${total}")

