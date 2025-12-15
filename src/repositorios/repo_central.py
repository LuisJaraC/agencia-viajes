from .usuario_repo import UsuarioRepo
from .rol_repo import RolRepo

# DI hasta UsuarioRepo, completar el resto
class RepoCentral():
    def __init__(self, mydb):
        self.UsuarioRepo = UsuarioRepo(mydb)
        self.RolRepo = RolRepo(mydb)