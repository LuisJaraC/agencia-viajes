class DestinoControl:
    def __init__(self, servicio_central):
        self.servicio_central = servicio_central

    def leer_destino(self):
        self.servicio_central.destino_servicio.leer_destino()
    def crear_destino(self):
        self.servicio_central.destino_servicio.crear_destino()
    def actualizar_destino(self):
        self.servicio_central.destino_servicio.actualizar_destino()
    def cambiar_estado(self):
        self.servicio_central.destino_servicio.cambiar_estado()