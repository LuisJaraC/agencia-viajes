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
    
    def menu_destino(self):
        print("\n          Menu Agencia \n")
        
        mensaje = """
        1. Ver destinos
        2. Crear destino
        3. Actualizar destino
        4. Activar/desactivar destino
        5. Cerrar sesión
        """
        print(textwrap.dedent(mensaje))
        opc = input("Elección: ")

        if opc == "3":
            print("Cerrando sesion...")
            
        return opc
    
    def crear_destino(self):
        print("\n             Crear Destino \n")
        nombre = input("Nombre: ")
        descripcion = input("Descripcion: ")
        precio_base = input("Precio: $")
        print("\n Creando destino ... \n")
        print("\n Destino Creado \n")


        return (nombre, descripcion, precio_base)
    
    def actualizar_destino(self):
        print("\n             Actualizar Destino \n")
        id_destino = input("Ingrese ID de fila a modificar: ")
        campo = input("Ingrese campo a modificar: ")
        dato = input("Ingrese nuevo dato: ")
        print("\n Actualizando destino ... \n")
        print("\n Destino actualizado ... \n")

        return (id_destino, campo, dato) 
           
    def cambio_estado(self):
        print("\n          Activar/desactivar destino \n")
        opc = input("""
            Ingrese el ID de destino a activar/desactivar\n
            -> Puedes revisarlo en el menu anterior <-
            
            Elección: """
                    )
        print("\n Cambio de estado exitoso...\n")
        return opc