class DestinoControl:
    def __init__(self, servicio_central):
        self.servicio_central = servicio_central

    def leer_destino(self):
        self.servicio_central.destino_servicio.leer_destino()