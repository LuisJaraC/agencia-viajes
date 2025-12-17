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
                usuario = self.servicio_central.usuario_servicio.iniciar_sesion(credenciales)
                print(f"tipo: {type(usuario.id_rol)}, dato: {usuario.id_rol}")

                # bifucarción. A que sub controlador se manda el flujo
                if usuario.id_rol == 1:
                    self.flujo_cliente(usuario)
                elif usuario.id_rol == 2:
                    self.flujo_adm()
                elif usuario.id_rol == 3:
                    self.flujo_agencia()
            elif opc1 == "2":
                credenciales_registro = vista_central.registrar()
                self.servicio_central.usuario_servicio.registrar(credenciales_registro)
            elif opc1 == "3":
                break;

    def flujo_cliente(self, usuario_obj):
        # opc2 es la accion que quiere realizar el cliente dentro de sus posibilidades
        # expuetas en el menu cliente
        vista_cliente = ClienteVista()

        while True:
            opc = vista_cliente.menu_cliente()
            if opc == "1":
                self.reserva_control.crear_reserva(usuario_obj)
            elif opc == "2":
                # revisar historial de reservar de este cliente
                pass
            elif opc == "3":
                break

    def flujo_adm(self):
        vista_adm = AdmVista()

        while True:
            opc3 = vista_adm.menu_adm()
            if opc3 == "1":
                opc_adm_1 = vista_adm.menu_gestion()
                self.submenu_adm(opc_adm_1)
            elif opc3 == "2":
                # Reporte global
                pass
            elif opc3 == "3":
                break

    def submenu_adm(self, opc_adm_1):
            if opc_adm_1 == "1":
                self.servicio_central.usuario_servicio.leer_usuario()
            elif opc_adm_1 == "2":
                pass
            elif opc_adm_1 == "3":
                self.flujo_adm("3")
            
        

    def flujo_agencia(self):
        vista_agencia = AgenciaVista()
        opc = vista_agencia.menu_agencia()
        