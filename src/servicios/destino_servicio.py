class DestinoServicio():
    def __init__(self, repo_central):
        self.repo_central = repo_central

    def leer_destino(self):
        self.repo_central.DestinoRepo.leer_destino()