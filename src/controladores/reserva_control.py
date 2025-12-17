from src.vista.reserva_vista import ReservaVista


class ReservaControl:
    def __init__(self, servicio_central):
        self.servicio_central = servicio_central
        self.reservar_vista = ReservaVista()

    def crear_reserva(self):
        paquetes_disponibles = self.servicio_central.paquete_servicio.leer_paquetes_disponibles()

        # antes de tomar los datos, se debe entregar los paquetes disponibles para reservar
        datos_reserva = self.reservar_vista.tomar_datos_reserva(paquetes_disponibles)

        if datos_reserva == None:
            return
        else:
            self.servicio_central.reserva_servicio.generar_reserva()

    def leer_reserva(self):
        self.servicio_central.reserva_servicio.leer_reserva()