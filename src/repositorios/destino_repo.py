import mysql.connector


class DestinoRepo():
    def __init__(self, mydb):
        self.mydb = mydb

    def leer_destino(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM destino")
        resultados = cursor.fetchall()

        for destino in resultados:
            print(destino)
        cursor.close()
