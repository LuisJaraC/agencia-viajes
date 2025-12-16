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
    
    def crear_destino(self,destino):
        cursor = self.mydb.cursor()

        sql = "INSERT INTO destino (nombre,descripcion,precio_base)"\
        "VALUES (%s,%s,%s)"
        val = (
            destino.nombre,
            destino.descripcion,
            destino.precio_base
        )

        try:
            cursor.execute(sql,val)
            self.mydb.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            cursor.close()
            raise ValueError(f"Error : {e}")

    def actualizar_destino(self,id_destino,var_mod,nuevo_dato):
        cursor = self.mydb.cursor()

        sql = f"UPDATE destino SET {var_mod} = %s WHERE id_destino = %s"
        val = (nuevo_dato, id_destino)

        cursor.execute(sql, val)
        self.mydb.commit()
        cursor.close()
