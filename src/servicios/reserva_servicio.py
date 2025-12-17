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

        # ahora actualizamos los cupos en paquetes
        cupos_antiguos = self.repo_central.PaqueteRepo.leer_cupos_paquete(id_paquete)
        cupos_actualizado = cupos_antiguos[0] - cant_personas_reserva
        var_mod = "cupos"
        

        self.repo_central.PaqueteRepo.actualizar_paquete(id_paquete,var_mod,cupos_actualizado)

    def leer_reserva_usuario(self, usuario_obj):

        id_user = usuario_obj.id_user
        reservas_usuario = self.repo_central.ReservaRepo.leer_reserva_usuario(id_user)
        return reservas_usuario
    def leer_reserva(self):
        return self.repo_central.ReservaRepo.leer_reserva()
    
    def obtener_total(self):
        lista_reservas = self.leer_reserva()

        transacciones = 0
        personas = 0
        total_ingresos = 0

        if lista_reservas:
            transacciones = len(lista_reservas)

            for reserva in lista_reservas:
                personas += int(reserva.ctd_personas)

                total_ingresos += int(reserva.precio_pactado)

        return{
            "transacciones": transacciones,
            "personas": personas,
            "ingresos": total_ingresos
        }

