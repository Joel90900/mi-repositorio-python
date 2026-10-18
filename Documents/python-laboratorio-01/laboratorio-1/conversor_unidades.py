kilometros = float(input("Ingresa una distancia en kilómetros: "))

metros = kilometros * 1000
centimetros = kilometros * 100_000
millas = kilometros * 0.621371

print("\nConversión de distancia")
print("-----------------------")
print(f"Kilómetros:  {kilometros:g} km")
print(f"Metros:      {metros:g} m")
print(f"Centímetros: {centimetros:g} cm")
print(f"Millas:      {millas:g} mi (aprox.)")
