class UsuarioControl:
    def __init__(self, servicio_central):
        self.servicio_central = servicio_central

    def leer_usuario(self):
        self.servicio_central.usuario_servicio.leer_usuario()
    def crear_usuario(self):
        self.servicio_central.usuario_servicio.crear_usuario()
    def actualizar_usuario(self):
        self.servicio_central.usuario_servicio.actualizar_usuario()
    