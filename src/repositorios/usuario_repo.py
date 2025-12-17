import mysql.connector
from ..modelos.usuario_modelo import Usuario

class UsuarioRepo():
    def __init__(self, mydb):
        self.mydb = mydb

    def leer_usuario(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM usuario")
        resultados = cursor.fetchall()

        # Convertimos tupla en una lista de objetos
        #id_user= [0], nombre=[1], apellido=[2], email=[3], passwd=[4], id_rol=[5], fecha_reg=[6], is_active=[7]
        lista_objetos_usuario = []
        for tupla in resultados:
            rol_obj = Usuario(
                id_user=tupla[0],
                nombre=tupla[1],
                id_rol=tupla[5],
                is_active=tupla[7]
                )
            lista_objetos_usuario.append(rol_obj)
            
        cursor.close()
        
        return lista_objetos_usuario

    def leer_email_passwd_usuario(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT email, passwd, id_rol FROM usuario")
        resultados = cursor.fetchall()

        cursor.close()
        return resultados

    def crear_usuario(self, user):
        cursor = self.mydb.cursor()
        
        sql = "INSERT INTO usuario (nombre, apellido, email, passwd, id_rol)"\
        "VALUES (%s,%s,%s,%s,%s)"

        val=(
            user.nombre,
            user.apellido,
            user.email,
            user.passwd,
            1
        )

        try:
            cursor.execute(sql, val)
            self.mydb.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            cursor.close()
            raise ValueError(f"Error: {err}")
        
    def actualizar_usuario(self, id_usuario, var_mod, nuevo_dato):
        cursor = self.mydb.cursor()

        sql = f"UPDATE usuario SET {var_mod} = %s WHERE id_usuario = %s"
        val = (nuevo_dato, id_usuario)

        cursor.execute(sql, val)

        self.mydb.commit()
        cursor.close()

    def estado_usuario (self, id_user):
        cursor = self.mydb.cursor()
        # se utiliza un "NOT is_active" como inversor logico, para setear el valor opuesto del bool
        sql = "UPDATE destino SET is_active = NOT is_active WHERE id_destino = %s"
        val = (id_user,)

        try:
            cursor.execute(sql, val)
            self.mydb.commit()
            #se utiliza cursor.rowcount para validar si se hicieron cambios 
            # > 0 si hubo cambio, == 0 no se encontró usuario o no hubieron cambios
            if cursor.rowcount > 0:
                print(f"Estado del usuario {id_user} cambiado exitosamente")
                return True
            else:
                print("No se encontró el usuario")
                return False
        except mysql.connector.Error as e:
            print(f"Error al cambiar estado: {e}")
            return False
        finally:
            cursor.close()