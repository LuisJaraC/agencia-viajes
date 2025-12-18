import mysql.connector
from src.modelos.paquetes_modelo import Paquete


class PaqueteRepo():
    def __init__(self, mydb):
        self.mydb = mydb

    def leer_paquetes_todos(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM paquete_turistico")
        resultados = cursor.fetchall()
        cursor.close()

        lista_obj = []
        for i in resultados:
            paquete_obj = Paquete(
                id_paquete=i[0],
                nombre_paq=i[1],
                precio=i[2],
                cupos=i[3],      
                stock=i[4],      
                fecha_ini=i[5],
                fecha_fin=i[6],
                is_active=i[7]
            )
            lista_obj.append(paquete_obj)

        return lista_obj

    def leer_paquetes_disponibles(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM paquete_turistico WHERE is_active = TRUE ORDER BY fecha_ini ASC")
        resultados = cursor.fetchall()

        cursor.close()

        return resultados
    
    def leer_cupos_paquete(self, id_paquete):
        cursor = self.mydb.cursor()
        cursor.execute(f"SELECT cupos FROM paquete_turistico WHERE id_paquete = {id_paquete}")
        resultado = cursor.fetchone()

        cursor.close()
        return resultado

    
    def crear_paquete(self, paquete):
        cursor = self.mydb.cursor()

        sql = """
            INSERT INTO paquete_turistico 
            (nombre_paq, precio, cupos, stock, fecha_ini, fecha_fin, is_active) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        val = (
            paquete.nombre_paq,
            paquete.precio,
            paquete.cupos,
            paquete.stock,
            paquete.fecha_ini,
            paquete.fecha_fin,
            paquete.is_active
        )

        try:
            cursor.execute(sql, val)
            self.mydb.commit()

            id_generado = cursor.lastrowid 
            
            cursor.close()
            
            return id_generado 

        except mysql.connector.Error as err:
            cursor.close()
            print(f"Error al crear paquete: {err}")
            return None
        
    def actualizar_paquete(self,id_paquete,var_mod,nuevo_dato):
        cursor = self.mydb.cursor()

        sql = f"UPDATE paquete_turistico SET {var_mod} = %s WHERE id_paquete = %s"
        val = (nuevo_dato,id_paquete)

        cursor.execute(sql,val)
        self.mydb.commit()
        cursor.close()