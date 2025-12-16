from .usuario_control import UsuarioControl
from .rol_control import RolControl
from .destino_control import DestinoControl
from .paquete_control import PaqueteControl
from .reserva_control import ReservaControl
from .destino_paquete_control import DestinoPaqueteControl
from src.vista.vista_general import VistaGeneral
from src.vista.cliente_vista import ClienteVista
from src.vista.agencia_vista import AgenciaVista
from src.vista.adm_vista import AdmVista

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

        while True:
            opc1 = vista_central.vista_general()

            if opc1 == "1":
                credenciales = vista_central.iniciar_sesion()
                rol = self.servicio_central.usuario_servicio.iniciar_sesion(credenciales)

                # bifucarción. A que sub controlador se manda el flujo
                if rol == "1":
                    vista_cliente = ClienteVista()
                    opc2 = vista_cliente.menu_cliente()
                    self.flujo_cliente(opc2)
                elif rol == "2":
                    vista_adm = AdmVista()
                    opc3 = vista_adm.menu_adm()
                    self.flujo_adm(opc3)
                elif rol == "3":
                    vista_agencia = AgenciaVista()
                    opc4 = vista_agencia.menu_agencia()
                    self.flujo_agencia(opc4)
            elif opc1 == "2":
                credenciales_registro = vista_central.registrar()
                self.servicio_central.usuario_servicio.registrar(credenciales_registro)
            elif opc1 == "3":
                break;

    def flujo_cliente(self, opc2):
        # opc2 es la accion que quiere realizar el cliente dentro de sus posibilidades
        # expuetas en el menu cliente
        pass

    def flujo_adm(self, opc3):
        # mismo que flujo cliente
        pass

    def flujo_agencia(self, opc4):
        # mismo que flujo cliente
        pass
