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
                
                if usuario is None: # validacion en caso de que no haya match
                    print("\n[!] Error: Usuario no encontrado o contraseña incorrecta.")
                    continue
                print(f"DEBUG -> Usuario: {usuario.nombre}, Rol ID: {usuario.id_rol}")
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
                self.reserva_control.leer_reserva_usuario(usuario_obj)
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
                opc_adm_1 = vista_adm.menu_detalle_rep()
                self.submenu_reporte(opc_adm_1)
                
            elif opc3 == "3":
                break

    def submenu_adm(self, opc_adm_1):
            if opc_adm_1 == "1":
                lista_usuario = self.servicio_central.usuario_servicio.leer_usuario()
                for usuario in lista_usuario:
                    if str(usuario.id_rol) == "1":
                        print(f"ID: {usuario.id_user}, nombre: {usuario.nombre} {usuario.apellido}")
                        if usuario.is_active:
                            print("ACTIVO")
                        else:
                            print("BLOQUEADO")
            elif opc_adm_1 == "2":
                adm_vista = AdmVista()
                toggle = adm_vista.menu_toggle()
                if toggle:
                    self.servicio_central.usuario_servicio.actualizar_estado(toggle)    
            elif opc_adm_1 == "3":
                return
            
    def submenu_reporte(self,opc_rep):
        if opc_rep == "1":
            lista_reserva = self.reserva_control.leer_reserva()
            if not lista_reserva:
                print("No hay reservas registradas.")
            else:
                print("\n--- REPORTE DE RESERVAS ---")
                for reserva in lista_reserva:
                    print(reserva)
        elif opc_rep == "2":
            reporte = self.reserva_control.reporte_ventas()
            vista_adm = AdmVista()
            vista_adm.mostrar_total_ventas(reporte)
        else:
            return
    def flujo_agencia(self):
        vista_agencia = AgenciaVista()

        while True:
            opc = vista_agencia.menu_agencia()
            if opc == "1":
                opc_destino = vista_agencia.menu_destino()
                self.submenu_destino(opc_destino)
            elif opc == "2":
                self.paquete_control.menu_gestion_paquetes()
                pass
            elif opc== "3":
                break

    def submenu_destino(self,opc):
        vista_agencia = AgenciaVista()
        if opc == "1":
            lista_destinos = self.servicio_central.destino_servicio.leer_destino()
            for destino in lista_destinos:
                print(f"ID: {destino.id_destino}, nombre: {destino.nombre}, precio:{destino.precio_base}")
                if destino.is_active:
                    print("ACTIVO")
                else:
                    print("BLOQUEADO")
            
        elif opc == "2":
            lista_crear = vista_agencia.crear_destino()
            self.servicio_central.destino_servicio.crear_destino(lista_crear)
        elif opc == "3":
            lista_actualizar = vista_agencia.actualizar_destino()
            if lista_actualizar:
                match = self.servicio_central.destino_servicio.actualizar_destino(lista_actualizar)
                if match:
                    print("Actualización exitosa.")
                else:
                    print("Error: No se pudo actualizar (ID incorrecto o Campo no permitido).")
        elif opc =="4":
            cambio_estado = vista_agencia.cambio_estado()
            if cambio_estado:
                self.servicio_central.destino_servicio.cambiar_estado(cambio_estado)    
        elif opc == "5":
            return
            

        