from src.vista.paquete_vista import PaqueteVista

class PaqueteControl:
    def __init__(self, servicio_central):
        self.servicio_central = servicio_central
        self.paquete_vista = PaqueteVista()

    def menu_gestion_paquetes(self):

        while True:
            opc = self.paquete_vista.crear_o_actualizar_estado()
            
            if opc == "1":
                self.crear_paquete_completo()
            elif opc == "2":
                self.activar_desactivar_paquete()
            elif opc == "3":
                break 
    
    def crear_paquete_completo(self):
        """
        Orquesta el flujo complejo de creación:
        1. Pedir datos básicos -> 2. Pedir destinos -> 3. Enviar a servicio
        """
        datos_basicos = self.paquete_vista.tomar_datos_nuevo_paquete()
        if datos_basicos is None: 
            return 

        lista_destinos = self.servicio_central.destino_servicio.leer_todos_los_destinos()
        
        if not lista_destinos:
            print("Error: No hay destinos registrados y activos para armar paquetes.")
            return

        ids_destinos = self.paquete_vista.seleccionar_destinos(lista_destinos)
        
        if not ids_destinos: 
            print("Debe seleccionar al menos un destino.")
            return

        self.servicio_central.paquete_servicio.crear_paquete_con_destinos(
            nombre=datos_basicos['nombre'],
            cupos=datos_basicos['cupos'],
            fecha_ini=datos_basicos['fecha_ini'],
            fecha_fin=datos_basicos['fecha_fin'],
            ids_destinos=ids_destinos
        )

    def activar_desactivar_paquete(self):
        lista_paquetes = self.servicio_central.paquete_servicio.leer_paquetes_todos()
        
        paquete_seleccionado = self.paquete_vista.mostrar_lista_paquete(lista_paquetes)
   
        if paquete_seleccionado:
            self.servicio_central.paquete_servicio.activar_desactivar_paquete(paquete_seleccionado)

    def leer_paquete_disponibles(self):
        resultados = self.servicio_central.paquete_servicio.leer_paquete()

        return resultados