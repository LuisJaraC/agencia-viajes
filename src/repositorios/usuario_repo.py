import mysql.connector


class UsuarioRepo():
    def __init__(self, mydb):
        self.mydb = mydb

    def leer_usuario(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM usuario")
        resultados = cursor.fetchall()

        for user in resultados:
            print(user)
        cursor.close()

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

    # def eliminar_usuario (self):
        # pass

