
print("Ingresa dos números enteros.")
a = int(input("Número 1: "))
b = int(input("Número 2: "))

print("\nPredicción: antes de probar otros valores, intenta adivinar el resultado.")
print(f"Número 1: {a}")
print(f"Número 2: {b}")

print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")

if b != 0:
    print(f"División: {a / b}")
    print(f"División entera: {a // b}")
    print(f"Residuo: {a % b}")
else:
    print("División: No se puede dividir entre 0")
    print("División entera: No se puede dividir entre 0")
    print("Residuo: No se puede dividir entre 0")
