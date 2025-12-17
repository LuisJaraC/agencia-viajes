import mysql.connector
from src.modelos.destino_modelo import Destino

class DestinoRepo():
    def __init__(self, mydb):
        self.mydb = mydb

    def leer_destino(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM destino")
        resultados = cursor.fetchall()

        lista_objetos = []
        for res in resultados:
            destino = Destino(
                id_destino=res[0],
                nombre=res[1],
                descripcion=res[2],
                precio_base=res[3],
                is_active=res[4]
                )
            lista_objetos.append(destino)
        cursor.close()
        return lista_objetos
    
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

        try:
            cursor.execute(sql, val)
            self.mydb.commit()
            
            # Verificamos si hubo cambios
            if cursor.rowcount > 0:
                return True
            return False
            
        except Exception as e:
            print(f"Error BD: {e}")
            return False
        finally:
            cursor.close()

    def cambiar_estado(self, id_destino):
        cursor = self.mydb.cursor()
        sql = "UPDATE destino SET is_active = NOT is_active WHERE id_destino = %s"
        val = (id_destino,)

        try:
            cursor.execute(sql, val)
            self.mydb.commit()

            if cursor.rowcount > 0:
                print(f"Estado del destino {id_destino} cambiado exitosamente")
                return True
            else:
                print("No se encontró el destino")
                return False
        except mysql.connector.Error as e:
            print(f"Error al cambiar estado: {e}")
            return False
        finally:
            cursor.close()