import mysql.connector


class ReservaRepo():
    def __init__(self, mydb):
        self.mydb = mydb

    def leer_reserva(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM reserva")
        resultados = cursor.fetchall()

        for res in resultados:
            print(res)
        cursor.close()

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
            self.leer_reserva()
            return True
        except mysql.connector.Error as err:
            cursor.close()
            raise ValueError(f"Error: {err}")
        
        
