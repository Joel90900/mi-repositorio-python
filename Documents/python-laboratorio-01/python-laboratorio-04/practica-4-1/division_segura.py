
try:
    dividendo = float(input("Dividendo: "))
    divisor = float(input("Divisor: "))
    resultado = dividendo / divisor
except ValueError:
    print("Entrada no numérica: escribe números válidos.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
else:
    print("Resultado:", resultado)
finally:
    print("Operación de división terminada.")

