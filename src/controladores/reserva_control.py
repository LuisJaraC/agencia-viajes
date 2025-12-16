class ReservaControl:
    def __init__(self, servicio_central):
        self.servicio_central = servicio_central

    def leer_reserva(self):
        self.servicio_central.reserva_servicio.leer_reserva()