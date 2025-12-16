class PaqueteServicio():
    def __init__(self, repo_central):
        self.repo_central = repo_central

    def leer_paquete(self):
        self.repo_central.PaqueteRepo.leer_paquete()