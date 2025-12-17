from getpass import getpass
import textwrap

class VistaGeneral():
    def __init__(self):
        pass

    def vista_general(self):
        print("          Pantalla principal")

        mensaje = """
            1. Inicio sesión
            2. Registro
            3. Cerrar Sesión
            """
        print(textwrap.dedent(mensaje))
            
        opc =input("Eleccion: ")

        return opc

    def iniciar_sesion(self):
        print("\n             Inicio Sesion \n")
        email = input("Email: ")
        passwd = getpass("Contraseña: ")
        print("\n Iniciando sesion ... \n")

        return (email, passwd)

    def registrar(self):
        print("\n          Registro  \n")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        email = input("Email: ")
        passwd = getpass("Contraseña: ")

        return (nombre, apellido, email, passwd)
