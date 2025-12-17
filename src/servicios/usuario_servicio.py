from src.modelos.usuario_modelo import Usuario
import bcrypt


class UsuarioServicio():
    def __init__(self, repo_central):
        self.repo_central = repo_central

    def iniciar_sesion(self, credenciales):
        
       # resultados_bd[0] es email
       # resultados_bd[1] es passwd
       # resultados_bd[2] es rol
        resultados_bd = self.repo_central.UsuarioRepo.leer_email_passwd_usuario()
        pw = credenciales[1]
        for i in resultados_bd:
            if i[0] == credenciales[0] and bcrypt.checkpw(pw.encode('utf-8'), i[1].encode('utf-8')):
                print(f"acceso concedido: {i[2]}")
                return i[2]



    def registrar(self, credenciales_registro):
        # [0] nombre; [1] apellido ; [2] email; [3] contraseña
        resultados_bd = self.repo_central.UsuarioRepo.leer_email_passwd_usuario()
        encontrado = False

        for i in resultados_bd:
            if i[0] == credenciales_registro[2]:
                print("email ya registrado")
                encontrado = True
        if encontrado == False:
            pw = credenciales_registro[3]
            salt = bcrypt.gensalt()
            passwd = bcrypt.hashpw(pw.encode('utf-8'), salt).decode('utf-8') # .decode('utf-8') convierte bytes a string
            usuario = Usuario(
                        nombre=credenciales_registro[0], 
                        apellido=credenciales_registro[1], 
                        email=credenciales_registro[2], 
                        passwd=passwd
            )
            self.repo_central.UsuarioRepo.crear_usuario(usuario)


    def leer_usuario(self):
        self.repo_central.UsuarioRepo.leer_usuario()
    
    def crear_usuario(self):
        self.repo_central.UsuarioRepo.crear_usuario()
    
    def actualizar_usuario(self):
        self.repo_central.UsuarioRepo.actualizar_usuario()
    
    def actualizar_estado(self):
        self.repo_central.UsuarioRepo.estado_usuario()