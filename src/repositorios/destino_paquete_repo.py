import mysql.connector


class DestinoPaqueteRepo():
    def __init__(self, mydb):
        self.mydb = mydb

    def leer_destino_paquete(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM destino_paquete")
        resultados = cursor.fetchall()

        for dp in resultados:
            print(dp)
        cursor.close()