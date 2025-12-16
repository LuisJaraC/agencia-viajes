from .usuario_control import UsuarioControl
from .rol_control import RolControl
from .destino_control import DestinoControl
from .paquete_control import PaqueteControl
from .reserva_control import ReservaControl
from .destino_paquete_control import DestinoPaqueteControl
from src.vista.vista_general import VistaGeneral

class ControladorCentral():
    def __init__(self, servicio_central):
        self.servicio_central = servicio_central
        self.usuario_control = UsuarioControl(servicio_central)
        self.rol_control = RolControl(servicio_central)
        self.destino_control = DestinoControl(servicio_central)
        self.paquete_control = PaqueteControl(servicio_central)
        self.reserva_control = ReservaControl(servicio_central)
        self.destino_paquete_control = DestinoPaqueteControl(servicio_central)

    def ejecutar(self):
        
        vista_central = VistaGeneral()
        opc = vista_central.vista_general()

        if opc == "1":
            print("dentro de if")
            credenciales = vista_central.iniciar_sesion()
            self.servicio_central.usuario_servicio.iniciar_sesion(credenciales)
        if opc == "2":
            credenciales_registro = vista_central.registrar()
            self.servicio_central.usuario_servicio.registrar(credenciales_registro)
        