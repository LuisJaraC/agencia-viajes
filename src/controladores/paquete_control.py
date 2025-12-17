class PaqueteControl:
    def __init__(self, servicio_central):
        self.servicio_central = servicio_central

    def leer_paquete_disponibles(self):
        resultados = self.servicio_central.paquete_servicio.leer_paquete()

        return resultados