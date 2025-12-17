import mysql.connector


class PaqueteRepo():
    def __init__(self, mydb):
        self.mydb = mydb

    def leer_paquetes_disponibles(self):
        cursor = self.mydb.cursor()

        # Traemos solo los paquetes disponibles, por orden en la fecha de inicio
        cursor.execute("SELECT * FROM paquete_turistico WHERE is_active = TRUE ORDER BY fecha_ini ASC")
        resultados = cursor.fetchall()

        cursor.close()

        return resultados
    
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