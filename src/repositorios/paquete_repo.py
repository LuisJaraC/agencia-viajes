import mysql.connector


class PaqueteRepo():
    def __init__(self, mydb):
        self.mydb = mydb

    def leer_paquete(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM paquete_turistico")
        resultados = cursor.fetchall()

        for paq in resultados:
            print(paq)
        cursor.close()