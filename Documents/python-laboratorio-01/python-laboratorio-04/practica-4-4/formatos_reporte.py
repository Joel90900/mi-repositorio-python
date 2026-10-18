# 4. Polimorfismo / Ejercicio — Formatos de reporte
# Clases ReporteTexto y ReporteResumen que comparten el método generar(datos).
# Se recorre la lista llamando a generar() sin necesidad de usar if para verificar el tipo.

class ReporteTexto:
    def generar(self, datos):
        elementos = ", ".join(str(d) for d in datos)
        return f"Reporte detallado: [{elementos}]"


class ReporteResumen:
    def generar(self, datos):
        return f"Resumen: se procesaron {len(datos)} registros en total."


datos_muestra = ["Teclado", "Mouse", "Monitor", "Cables"]

reportes = [ReporteTexto(), ReporteResumen()]

for reporte in reportes:
    # Llamada polimórfica: no importa la clase concreta mientras responda a generar()
    print(reporte.generar(datos_muestra))

