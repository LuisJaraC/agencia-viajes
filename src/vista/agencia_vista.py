import textwrap

class AgenciaVista:
    def __init__(self):
        pass

    def menu_agencia(self):
        print("\n          Menu Agencia \n")
        
        mensaje = """
        1. Gestionar destinos
        2. Gestionar paquetes
        3. Cerrar sesión
        """
        print(textwrap.dedent(mensaje))
        opc = input("Elección: ")

        if opc == "3":
            print("Cerrando sesion...")
            
        return opc