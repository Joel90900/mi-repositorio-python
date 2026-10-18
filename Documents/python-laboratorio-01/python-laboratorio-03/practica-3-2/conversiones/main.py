import unidades

kilometros = float(input("Kilómetros: "))
print(f"{kilometros} km = {unidades.kilometros_a_metros(kilometros)} m")

celsius = float(input("Grados Celsius: "))
print(f"{celsius} °C = {unidades.celsius_a_fahrenheit(celsius):.2f} °F")