print("=== FICHA PERSONAL ===")
nombre = input("Ingrese su nombre: ")
ciudad = input("Ingrese su ciudad: ")
edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura en metros: "))

print("\n=== DATOS PERSONALES ===")
print(f"Nombre: {nombre}")
print(f"Ciudad: {ciudad}")
print(f"Edad: {edad} años")
print(f"Estatura: {estatura:.2f} m")

# Operaciones con dos números enteros
print("\n=== OPERACIONES ENTRE NÚMEROS ===")
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entera = num1 // num2
residuo = num1 % num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"División entera: {division_entera}")
print(f"Residuo: {residuo}")
