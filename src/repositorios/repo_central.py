from .usuario_repo import UsuarioRepo

# DI hasta UsuarioRepo, completar el resto
class RepoCentral():
    def __init__(self, mydb):
        self.UsuarioRepo = UsuarioRepo(mydb)