from .usuario_servicio import UsuarioServicio
from .rol_servicio import RolServicio

class ServiciosCentral():
    def __init__(self, repo_central):
        self.usuario_servicio = UsuarioServicio(repo_central)
        self.rol_servicio = RolServicio(repo_central)

    