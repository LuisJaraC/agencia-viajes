from src.modelos.usuario_modelo import Usuario
import bcrypt


class UsuarioServicio():
    def __init__(self, repo_central):
        self.repo_central = repo_central

    def iniciar_sesion(self, credenciales):
        pw_input = credenciales[1]
        email_input = credenciales[0]
       # id_user ; nombre ; apellido ; email
       # passwd ; id_rol ; fecha_reg ; is_active
        resultados_bd = self.repo_central.UsuarioRepo.leer_usuario()
        for usuario in resultados_bd:
            if usuario.email == email_input and bcrypt.checkpw(pw_input.encode('utf-8'), usuario.passwd.encode('utf-8')): # metodo para comparar hash de contraseñas entre credenciales y bd
                print(f"acceso concedido: {usuario.nombre} {usuario.apellido}")
                return (usuario)



    def registrar(self, credenciales_registro):
        # [0] nombre; [1] apellido ; [2] email; [3] contraseña
        email_input = credenciales_registro[2]
        resultados_bd = self.repo_central.UsuarioRepo.leer_usuario()
        encontrado = False

        for usuario in resultados_bd:
            if usuario.email == email_input:
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
            print("Registro exitoso!")


    def leer_usuario(self):
        return self.repo_central.UsuarioRepo.leer_usuario()
    
    def crear_usuario(self):
        self.repo_central.UsuarioRepo.crear_usuario()
    
    def actualizar_usuario(self):
        self.repo_central.UsuarioRepo.actualizar_usuario()
    
    def actualizar_estado(self, id_user):
        return self.repo_central.UsuarioRepo.estado_usuario(id_user)