from src.modelos.reserva_modelo import Reserva

class ReservaServicio():
    def __init__(self, repo_central):
        self.repo_central = repo_central

    # generar reserva tiene por objetivos:
    # 1. Validar si los cupos requeridos están en el rango de los disponibles
    # 2. Calcular el valor total a pagar por el usuario
    # 3. Retornar None si no hay cupos diponibles o retornar el precio total para la confirmacion del usuario
    def generar_reserva(self, paquete_obj, cant_personas_reserva):
        
        cupos_disp = paquete_obj.cupos
        precio = paquete_obj.precio

        if cupos_disp < cant_personas_reserva:
            return None
        else: 
            total_pagar = precio * cant_personas_reserva
            return total_pagar
        
    def confirmar_reserva(self, usuario, precio_final_o_none, paquete):
        # llamar a reserva repo crear
        # actualizar cupos disp en ese paquete, llamar a repo paquetes actualizar




        pass

    def leer_reserva(self):
        self.repo_central.ReservaRepo.leer_reserva()