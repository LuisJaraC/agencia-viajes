class UsuarioServicio():
    def __init__(self, repo_central):
        self.repo_central = repo_central

    def leer_usuario(self):
        self.repo_central.UsuarioRepo.leer_usuario()
    
    def crear_usuario(self):
        self.repo_central.UsuarioRepo.crear_usuario()
    
    def actualizar_usuario(self):
        self.repo_central.UsuarioRepo.actualizar_usuario()