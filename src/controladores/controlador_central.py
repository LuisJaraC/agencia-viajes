from .usuario_control import UsuarioControl
from .rol_control import RolControl

# DI para usuario, completar para el resto
class ControladorCentral():
    def __init__(self, servicio_central):
        self.usuario_control = UsuarioControl(servicio_central)
        self.rol_control = RolControl(servicio_central)

    def ejecutar(self):
        
        self.rol_control.leer_rol()
        self.usuario_control.leer_usuario()
        