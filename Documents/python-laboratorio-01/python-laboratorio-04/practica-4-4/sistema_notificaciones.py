# Reto — Sistema de notificaciones
# Clase Notificacion con dos especializaciones: NotificacionCorreo y NotificacionConsola.
# Ambas implementan enviar(mensaje) de manera distinta (polimorfismo).
#
# Reflexión técnica:
# - Beneficio de una operación común: El código que envía mensajes no necesita saber
#   si se trata de correo, consola, SMS o webhook; solo invoca .enviar() (desacoplamiento).
# - Responsabilidades externas: La validación del destinatario, conexión de red o lógica
#   del negocio de cuándo se envía una alerta deben permanecer fuera de la clase individual.

class Notificacion:
    def enviar(self, mensaje):
        raise NotImplementedError("Las subclases deben implementar el método enviar")


class NotificacionCorreo(Notificacion):
    def __init__(self, destinatario):
        self.destinatario = destinatario

    def enviar(self, mensaje):
        return f"[CORREO -> {self.destinatario}] Asunto: Notificación del Sistema | Mensaje: {mensaje}"


class NotificacionConsola(Notificacion):
    def __init__(self, prefijo="[INFO]"):
        self.prefijo = prefijo

    def enviar(self, mensaje):
        return f"{self.prefijo} Alerta en pantalla: {mensaje}"


notificaciones = [
    NotificacionCorreo("admin@empresa.com"),
    NotificacionConsola("[SISTEMA-LOG]"),
    NotificacionCorreo("auditoria@empresa.com"),
]

mensaje_prueba = "El producto P002 (Mouse) se ha quedado sin existencias."

for n in notificaciones:
    print(n.enviar(mensaje_prueba))

