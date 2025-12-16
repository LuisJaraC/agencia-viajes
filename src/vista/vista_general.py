class VistaGeneral():
    def __init__(self):
        pass

    def vista_general(self):
        opc = input("""
                    Pantalla principal

            1. Inicio sesión
            2. Registro
            
            Eleccion: """)

        return opc

    def iniciar_sesion(self):
        print("\n             Inicio Sesion \n")
        email = input("Email: ")
        passwd = input("Contraseña: ")
        print("\n Iniciando sesion ... \n")

        return (email, passwd)

    def registrar(self):
        print("\n          Registro  \n")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        email = input("Email: ")
        passwd = input("Contraseña: ")

        return (nombre, apellido, email, passwd)