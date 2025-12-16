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
    
    def crear_paquete(self, paquete):
        cursor = self.mydb.cursor()

        sql = "INSERT INTO paquete (nombre_paq,precio,cupos,stock,fecha_ini,fecha_fin)"\
        "VALUES (%s,%s,%s,%s,%s,%s)"

        val = (
            paquete.nombre_paq,
            paquete.precio,
            paquete.cupos,
            paquete.stock,
            paquete.fecha_ini,
            paquete.fecha_fin
        )

        try:
            cursor.execute(sql,val)
            self.mydb.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            cursor.close()
            raise ValueError(f"Error: {err}")
        
    def actualizar_paquete(self,id_paquete,var_mod,nuevo_dato):
        cursor = self.mydb.cursor()

        sql = f"UPDATE paquete SET {var_mod} = %s WHERE id_paquete = %s"
        val = (nuevo_dato,id_paquete)

        cursor.execute(sql,val)
        self.mydb.commit()
        cursor.close()