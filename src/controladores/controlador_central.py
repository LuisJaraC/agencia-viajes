from .usuario_control import UsuarioControl
from .rol_control import RolControl
from .destino_control import DestinoControl
from .paquete_control import PaqueteControl
from .reserva_control import ReservaControl
from .destino_paquete_control import DestinoPaqueteControl

# DI para usuario, completar para el resto
class ControladorCentral():
    def __init__(self, servicio_central):
        self.usuario_control = UsuarioControl(servicio_central)
        self.rol_control = RolControl(servicio_central)
        self.destino_control = DestinoControl(servicio_central)
        self.paquete_control = PaqueteControl(servicio_central)
        self.reserva_control = ReservaControl(servicio_central)
        self.destino_paquete_control = DestinoPaqueteControl(servicio_central)

    def ejecutar(self):
        
        self.rol_control.leer_rol()
        self.usuario_control.leer_usuario()
        self.destino_control.leer_destino()
        self.paquete_control.leer_paquete()
        self.reserva_control.leer_reserva()
        self.destino_paquete_control.leer_destino_paquete()
        