class VistaGeneral():
    def __init__(self):
        pass

    def mostrarVista(self):
        print("""
            "\n           Bienvenido al menu principal\n" 
            "\n" 
            "¿Estas registrado?\n" 
            "\n" 
            "1. Registrate\n" 
            "2. Ingresa\n" \
            "0. Ingrese 0 para cerrar el programa"

""")
        opcion = input("\nIngresa opcion: ")
        return opcion