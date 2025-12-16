from .usuario_repo import UsuarioRepo
from .rol_repo import RolRepo
from .destino_repo import DestinoRepo
from .paquete_repo import PaqueteRepo
from .reserva_repo import ReservaRepo
from .destino_paquete_repo import DestinoPaqueteRepo

# DI hasta UsuarioRepo, completar el resto
class RepoCentral():
    def __init__(self, mydb):
        self.UsuarioRepo = UsuarioRepo(mydb)
        self.RolRepo = RolRepo(mydb)
        self.DestinoRepo = DestinoRepo(mydb)
        self.PaqueteRepo = PaqueteRepo(mydb)
        self.ReservaRepo = ReservaRepo(mydb)
        self.DestinoPaqueteRepo = DestinoPaqueteRepo(mydb)