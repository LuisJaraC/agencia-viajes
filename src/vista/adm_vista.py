class AdmVista:
    def __init__(self):
        pass

    def menu_adm(self):
        print("\n          Menu Administrador \n")
        opc = input("""
        1. Gestion usuarios
        2. Reporte global
        3. Cerrar sesión
        
        Elección: """)

        if opc == "3":
            print("Cerrando sesion...")
            
        return opc
    
    def menu_gestion(self):
        print("\n          Menu Administrador \n")
        opc_user = input("""
        1. Mostrar usuarios
        2. Desactivar usuario
        3. Volver al menu anterior
        
        Elección: """)   
        if opc_user == "3":
            print("Volviendo al menu anterior...")
        return opc_user