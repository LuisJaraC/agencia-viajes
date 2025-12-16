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