class Reserva:
    def __init__(self, id_reserva=None, fecha_creacion=None, ctd_personas=0, precio_pactado=0, id_user=None,id_paquete=None):
        self.id_reserva = id_reserva
        self.fecha_creacion = fecha_creacion
        self.ctd_personas = ctd_personas
        self.precio_pactado = precio_pactado
        self.id_user = id_user
        self.id_paquete = id_paquete

    def __str__(self):
        return f"Reserva[{self.id_reserva}]: {self.fecha_creacion} - {self.ctd_personas} - {self.id_paquete} - ${self.precio_pactado}"