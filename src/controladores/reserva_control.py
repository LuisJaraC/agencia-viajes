from src.vista.reserva_vista import ReservaVista

class ReservaControl:
    def __init__(self, servicio_central):
        self.servicio_central = servicio_central
        self.reservar_vista = ReservaVista()

    def crear_reserva(self):
        datos_reserva = self.reservar_vista.tomar_datos_reserva()
        # llamar a servicios 
        # probablemente el metodo tomar_datos_reserva tenga que obtener solo los paquetes activos
        # hay que ver como hacer eso

    def leer_reserva(self):
        self.servicio_central.reserva_servicio.leer_reserva()