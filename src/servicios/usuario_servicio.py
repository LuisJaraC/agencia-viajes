from src.modelos.usuario_modelo import Usuario

class UsuarioServicio():
    def __init__(self, repo_central):
        self.repo_central = repo_central

    def iniciar_sesion(self, credenciales):
        
       # credenciales[0] es email
       # credenciales[1] es passwd

        resultados_bd = self.repo_central.UsuarioRepo.leer_email_passwd_usuario()

        for i in resultados_bd:
            if i[0] == credenciales[0] and i[1] == credenciales[1]:
                print("comprobacion de email verificado en la bd")
                print(f'{i[0]} de la bd coincide con {credenciales[0]} ingresado por el usuario')
                print(f'{i[1]} de la bd coincide con {credenciales[1]} ingresado por el usuario')



    def registrar(self, credenciales_registro):
        print("estamos en registro usuario servicio")

    def leer_usuario(self):
        pass
    
    def crear_usuario(self):
        self.repo_central.UsuarioRepo.crear_usuario()
    
    def actualizar_usuario(self):
        self.repo_central.UsuarioRepo.actualizar_usuario()