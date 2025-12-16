class RolControl:
    def __init__(self, servicio_central):
        self.servicio_central = servicio_central

    def leer_rol(self):
        self.servicio_central.rol_servicio.leer_rol()