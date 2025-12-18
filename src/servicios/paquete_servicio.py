# Asegúrate de que el nombre del archivo del modelo coincida (paquete.py o paquetes_modelo.py)
from src.modelos.paquetes_modelo import Paquete 

class PaqueteServicio:
    def __init__(self, repo_central):
        self.repo_central = repo_central

    def crear_paquete_con_destinos(self, nombre, cupos, fecha_ini, fecha_fin, ids_destinos):
    
        
     
        precio_total = 0
        
       
        for id_dest in ids_destinos:
           
            destino_obj = self.repo_central.DestinoRepo.buscar_por_id(id_dest) 
            
            if destino_obj:
                precio_total += int(destino_obj.precio_base)
            else:
                print(f"Advertencia: Destino ID {id_dest} no encontrado, se ignorará en el precio.")
        
        print(f"Precio total calculado: ${precio_total}")

        # 2. Crear Objeto Paquete
        nuevo_paquete = Paquete(
            id_paquete=None,
            nombre_paq=nombre,
            precio=precio_total, 
            cupos=cupos,
            stock=True,          
            fecha_ini=fecha_ini,
            fecha_fin=fecha_fin,
            is_active=True       
        )

        id_paquete_generado = self.repo_central.PaqueteRepo.crear_paquete(nuevo_paquete)

        if id_paquete_generado:
            print(f"Paquete creado con ID: {id_paquete_generado}")
            
        
            for id_dest in ids_destinos:
                self.repo_central.DestinoPaqueteRepo.crear_relacion(id_dest, id_paquete_generado)
            
            print("Destinos vinculados correctamente.")
            return True
        else:
            print("Error crítico: No se pudo crear el paquete en BD.")
            return False

    def activar_desactivar_paquete(self, paquete):
     
        id_paquete = paquete.id_paquete
        var_mod = "is_active"

        # Invertimos el estado
        nuevo_estado = not paquete.is_active

        exito = self.repo_central.PaqueteRepo.actualizar_paquete(id_paquete, var_mod, nuevo_estado)
        
        if exito:
            estado_str = "ACTIVADO" if nuevo_estado else "DESACTIVADO"
            print(f"Paquete '{paquete.nombre_paq}' {estado_str} exitosamente.")
        
        return exito

    def leer_paquetes_todos(self):
      
        return self.repo_central.PaqueteRepo.leer_paquetes_todos()

    def leer_paquetes_disponibles(self):
     
        return self.repo_central.PaqueteRepo.leer_paquetes_disponibles()