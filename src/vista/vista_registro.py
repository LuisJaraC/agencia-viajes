from getpass import getpass
import bcrypt

class Registro:
    def __init__(self):
        pass
    def mostrarRegistro(self):
        print(
            "\n           Registro\n" 
            "\n" 
        )
        email = input("Ingrese su email: ")
        pw = getpass("ingrese su contraseña: ")