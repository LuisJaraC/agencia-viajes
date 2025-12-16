class DestinoPaqueteControl:
    def __init__(self, servicio_central):
        self.servicio_central = servicio_central

    def leer_destino_paquete(self):
        self.servicio_central.destino_paquete_servicio.leer_destino_paquete()