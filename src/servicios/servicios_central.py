from .usuario_servicio import UsuarioServicio

class ServiciosCentral():
    def __init__(self, mydb):
        self.usuario_servicio = UsuarioServicio(mydb)