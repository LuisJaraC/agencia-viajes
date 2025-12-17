from src.vista.reserva_vista import ReservaVista


class ReservaControl:
    def __init__(self, servicio_central):
        self.servicio_central = servicio_central
        self.reservar_vista = ReservaVista()

    def crear_reserva(self, usuario_obj):
        paquetes_disponibles = self.servicio_central.paquete_servicio.leer_paquetes_disponibles()

        # antes de tomar los datos, se debe entregar los paquetes disponibles para reservar
        datos_reserva = self.reservar_vista.tomar_datos_reserva(paquetes_disponibles)

        if datos_reserva == None:
            return
        else:
            # pasamos paquete de tupla a objeto
            paquete_tupla = datos_reserva[0]
            id_paquete = paquete_tupla[0]
            cupos = paquete_tupla[3]
            precio = paquete_tupla[2]

            id_usuario = usuario_obj.id_user

            cant_personas_reserva = datos_reserva[1]
            # validar cupos y mostrar monto total 
            precio_final_o_none = self.servicio_central.reserva_servicio.generar_reserva(cupos, precio, cant_personas_reserva)
            confirmacion = self.reservar_vista.confirmar_monto(precio_final_o_none)

            if confirmacion == "1":
                self.servicio_central.reserva_servicio.confirmar_reserva(id_paquete, id_usuario, cant_personas_reserva, precio_final_o_none)
            elif confirmacion == "2":
                return
            elif confirmacion == None:
                return

    def leer_reserva_usuario(self, usuario_obj):
        reservas_usuario = self.servicio_central.reserva_servicio.leer_reserva_usuario(usuario_obj)
        self.reservar_vista.mostrar_reservas_usuario(reservas_usuario)