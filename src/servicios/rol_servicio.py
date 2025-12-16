class RolServicio():
    def __init__(self, repo_central):
        self.repo_central = repo_central

    def leer_rol(self):
        self.repo_central.RolRepo.leer_rol()