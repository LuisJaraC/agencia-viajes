import textwrap
from datetime import datetime

class PaqueteVista:
    def __init__(self):
        pass
    
    def crear_o_actualizar_estado(self):
        print("\n          GESTIÓN DE PAQUETES (AGENCIA) \n")
        
        mensaje = """
        1. Crear Paquete (Armar con destinos)
        2. Activar/Desactivar Paquetes
        3. Volver al menú anterior
        """
        print(textwrap.dedent(mensaje))
        return input("Elección: ")

    def tomar_datos_nuevo_paquete(self):
        print("\n      PASO 1: DATOS BÁSICOS DEL PAQUETE ")
        
        try:
          
            nombre = input("Nombre del paquete: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
                return None
            
     
            cupos = int(input("Cupos disponibles: "))

       
            fecha_ini = self.__pedir_fecha("Fecha Inicio (YYYY-MM-DD): ")
            if not fecha_ini: return None 

            fecha_fin = self.__pedir_fecha("Fecha Fin (YYYY-MM-DD): ")
            if not fecha_fin: return None

            # Retornamos dict con datos básicos
            return {
                "nombre": nombre,
                "cupos": cupos,
                "fecha_ini": fecha_ini,
                "fecha_fin": fecha_fin
            }

        except ValueError:
            print("Error: Los cupos deben ser un número entero.")
            return None

    def seleccionar_destinos(self, lista_destinos):
 
        print("\n      PASO 2: SELECCIÓN DE DESTINOS ")
        print("Seleccione los destinos que compondrán este paquete:\n")
        
        # Mostramos los destinos disponibles con su precio base
        for dest in lista_destinos:
            print(f"ID: {dest.id_destino} | {dest.nombre} | Precio Base: ${dest.precio_base}")
            
        print("\nInstrucciones: Ingrese los IDs separados por comas (ej: 1, 3, 5)")
        entrada = input("Su selección: ")
        
        try:
            # Convertimos "1, 3" -> [1, 3]
            if not entrada.strip():
                return []
            
            ids_seleccionados = [int(x.strip()) for x in entrada.split(",")]
            return ids_seleccionados
        except ValueError:
            print("Error: Debe ingresar solo números separados por comas.")
            return []

    def mostrar_lista_paquete(self, lista_paquetes):
     
        if not lista_paquetes:
            print("No hay paquetes registrados.")
            return None
        
        print("\n      --- ACTIVAR / DESACTIVAR PAQUETES ---")
        for i, paq in enumerate(lista_paquetes):
            estado = "Activo" if paq.is_active else "Inactivo"
            print(f"{i+1}. {paq.nombre_paq} | ${paq.precio} | {estado}")
            
        print("0. Volver atrás")
        
        while True:
            try:
                opc = int(input("\nSeleccione un número de la lista: "))
                if opc == 0: return None
                
                if 1 <= opc <= len(lista_paquetes):
                    return lista_paquetes[opc - 1] 
                else:
                    print("Opción fuera de rango.")
            except ValueError:
                print("Debe ingresar un número.")

    def __pedir_fecha(self, mensaje):
        while True:
            fecha_str = input(mensaje)
            try:
                datetime.strptime(fecha_str, "%Y-%m-%d")
                return fecha_str
            except ValueError:
                print("Formato incorrecto. Use Año-Mes-Dia (ej: 2025-12-31)")
                retry = input("¿Intentar de nuevo? (s/n): ")
                if retry.lower() != 's':
                    return None