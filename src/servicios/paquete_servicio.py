class PaqueteServicio():
    def __init__(self, repo_central):
        self.repo_central = repo_central

    def leer_paquetes_disponibles(self):
        resultados = self.repo_central.PaqueteRepo.leer_paquetes_disponibles()

        return resultados