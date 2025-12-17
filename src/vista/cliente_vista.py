import textwrap

class ClienteVista:
    def __init__(self):
        pass

    def menu_cliente(self):
        print("\n          Menu Cliente \n")
        
        mensaje = """
        1. Realizar reserva de paquete turístico
        2. Consultar historial de reservas
        3. Cerrar sesión
        """
        print(textwrap.dedent(mensaje))
        opc = input("Elección: ")

        if opc == "3":
            print("Cerrando sesion...")
            
        return opc