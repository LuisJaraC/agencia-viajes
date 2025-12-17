import mysql.connector
from src.modelos.reserva_modelo import Reserva

class ReservaRepo():
    def __init__(self, mydb):
        self.mydb = mydb

    def leer_reserva(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM reserva")
        resultados = cursor.fetchall()

        lista_objetos = []
        for res in resultados:
            reserva = Reserva(
                id_reserva=res[0],
                fecha_creacion=res[1],
                ctd_personas=res[2],
                precio_pactado=res[3],
                id_user=res[4],
                id_paquete=res[5]
                )
            lista_objetos.append(reserva)
        cursor.close()
        return lista_objetos

    def leer_reserva_usuario(self, id_user):
        cursor = self.mydb.cursor()

        cursor.execute(f"SELECT * FROM reserva WHERE id_user = {id_user}")
        reservas_usuario = cursor.fetchall()
        cursor.close()

        lista_objetos = []

        for i in reservas_usuario:
            reserva_obj = Reserva(
                id_reserva=i[0],     
                fecha_creacion=i[1],  
                ctd_personas=i[2],    
                precio_pactado=i[3],
                id_user=i[4],
                id_paquete=i[5]
            )
            lista_objetos.append(reserva_obj)

        return lista_objetos

    def crear_reserva(self, reserva):
        cursor = self.mydb.cursor()

        sql = "INSERT INTO reserva (ctd_personas,precio_pactado,id_user,id_paquete)"\
        "VALUES (%s,%s,%s,%s)"
        val = (
            reserva.ctd_personas,
            reserva.precio_pactado,
            reserva.id_user,
            reserva.id_paquete
        )

        try:
            cursor.execute(sql, val)
            self.mydb.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            cursor.close()
            raise ValueError(f"Error: {err}")
        
        
