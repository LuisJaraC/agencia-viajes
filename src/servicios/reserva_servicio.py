class ReservaServicio():
    def __init__(self, repo_central):
        self.repo_central = repo_central

    def leer_reserva(self):
        self.repo_central.ReservaRepo.leer_reserva()