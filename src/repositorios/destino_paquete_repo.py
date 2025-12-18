import mysql.connector


class DestinoPaqueteRepo():
    def __init__(self, mydb):
        self.mydb = mydb

    def crear_relacion(self, id_destino, id_paquete):
        cursor = self.mydb.cursor()
        sql = "INSERT INTO destino_paquete (id_destino, id_paquete) VALUES (%s, %s)"
        
        try:
            cursor.execute(sql, (id_destino, id_paquete))
            self.mydb.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error al vincular destino-paquete: {err}")
            return False
        finally:
            cursor.close()

    def leer_destino_paquete(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM destino_paquete")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

    def leer_destino_paquete(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM destino_paquete")
        resultados = cursor.fetchall()

        for dp in resultados:
            print(dp)
        cursor.close()