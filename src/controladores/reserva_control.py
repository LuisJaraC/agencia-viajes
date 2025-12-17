from src.vista.reserva_vista import ReservaVista
from src.modelos.paquetes_modelo import Paquete


class ReservaControl:
    def __init__(self, servicio_central):
        self.servicio_central = servicio_central
        self.reservar_vista = ReservaVista()

    def crear_reserva(self, usuario):
        paquetes_disponibles = self.servicio_central.paquete_servicio.leer_paquetes_disponibles()

        # antes de tomar los datos, se debe entregar los paquetes disponibles para reservar
        datos_reserva = self.reservar_vista.tomar_datos_reserva(paquetes_disponibles)

        if datos_reserva == None:
            return
        else:
            # pasamos paquete de tupla a objeto
            paquete_tupla = datos_reserva[0]
            
            paquete_obj = Paquete(
                                None, paquete_tupla[1], paquete_tupla[2], paquete_tupla[3],
                                paquete_tupla[4], paquete_tupla[5], paquete_tupla[6], paquete_tupla[7]
                                )
            cant_personas_reserva = datos_reserva[1]
            # validar cupos y mostrar monto total 
            precio_final_o_none = self.servicio_central.reserva_servicio.generar_reserva(paquete_obj, cant_personas_reserva)
            confirmacion = self.reservar_vista.confirmar_monto(precio_final_o_none)

            if confirmacion == "1":
                self.servicio_central.reserva_servicio.confirmar_reserva(
                                                                        usuario, precio_final_o_none, 
                                                                        paquete_obj, cant_personas_reserva
                                                                        )
            elif confirmacion == "2":
                return

    def leer_reserva(self):
        self.servicio_central.reserva_servicio.leer_reserva()