from src.modelos.reserva_modelo import Reserva

class ReservaServicio():
    def __init__(self, repo_central):
        self.repo_central = repo_central

    # generar reserva tiene por objetivos:
    # 1. Validar si los cupos requeridos están en el rango de los disponibles
    # 2. Calcular el valor total a pagar por el usuario
    # 3. Retornar None si no hay cupos diponibles o retornar el precio total para la confirmacion del usuario
    def generar_reserva(self, cupos, precio, cant_personas_reserva):
        

        if cupos < cant_personas_reserva:
            return None
        else: 
            total_pagar = precio * cant_personas_reserva
            return total_pagar
        
    def confirmar_reserva(self, id_paquete, id_usuario, cant_personas_reserva, precio_final_o_none):
        # llamar a reserva repo crear
        # actualizar cupos disp en ese paquete, llamar a repo paquetes actualizar

        reserva = Reserva(
                ctd_personas=cant_personas_reserva, 
                precio_pactado=precio_final_o_none,
                id_user=id_usuario,
                id_paquete=id_paquete
                )
        
        self.repo_central.ReservaRepo.crear_reserva(reserva)
        
    def leer_reserva(self):
        return self.repo_central.ReservaRepo.leer_reserva()