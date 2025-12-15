from .usuario_control import UsuarioControl

# DI para usuario, completar para el resto
class ControladorCentral():
    def __init__(self, servicio_central):
        self.usuario_control = UsuarioControl(servicio_central)

    def ejecutar(self):
        pass