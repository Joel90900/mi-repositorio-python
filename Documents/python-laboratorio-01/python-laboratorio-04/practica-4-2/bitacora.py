

RESULTADOS_VALIDOS = ("aprobada", "fallida")

nombre = input("Nombre de la prueba: ").strip()

while True:
    resultado = input("Resultado (aprobada/fallida): ").strip().lower()
    if resultado in RESULTADOS_VALIDOS:
        break
    print("Escribe 'aprobada' o 'fallida'.")

observacion = input("Observación breve: ").strip()

with open("pruebas.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{nombre} | {resultado} | {observacion}\n")

print("Prueba registrada en pruebas.txt")

