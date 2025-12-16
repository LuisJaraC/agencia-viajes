class DestinoPaqueteServicio():
    def __init__(self, repo_central):
        self.repo_central = repo_central

    def leer_destino_paquete(self):
        self.repo_central.DestinoPaqueteRepo.leer_destino_paquete()