from .usuario_servicio import UsuarioServicio
from .rol_servicio import RolServicio
from .destino_servicio import DestinoServicio
from .paquete_servicio import PaqueteServicio
from .reserva_servicio import ReservaServicio
from .destino_paquete_servicio import DestinoPaqueteServicio

class ServiciosCentral():
    def __init__(self, repo_central):
        self.usuario_servicio = UsuarioServicio(repo_central)
        self.rol_servicio = RolServicio(repo_central)
        self.destino_servicio = DestinoServicio(repo_central)
        self.paquete_servicio = PaqueteServicio(repo_central)
        self.reserva_servicio = ReservaServicio(repo_central)
        self.destino_paquete_servicio = DestinoPaqueteServicio(repo_central)

    