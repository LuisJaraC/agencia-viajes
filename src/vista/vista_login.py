from getpass import getpass
import bcrypt

class Login:
    def __init__(self):
        pass
    def mostrarLogin(self):
        print(
            "\n           Login\n" 
            "\n" 
        )
        email = input("Ingrese su email: ")
        pw = getpass("ingrese su contraseña: ")