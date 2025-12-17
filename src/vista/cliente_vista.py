class ClienteVista:
    def __init__(self):
        pass

    def menu_cliente(self):
        print("\n          Menu Cliente \n")
        opc = input("""
        1. Realizar reserva de paquete turístico
        2. Consultar historial de reservas
        3. Cerrar sesión
        
        Elección: """)

        if opc == "3":
            print("Cerrando sesion...")
            
        return opc