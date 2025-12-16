import mysql.connector

class UsuarioRepo():
    def __init__(self, mydb):
        self.mydb = mydb

    def leer_usuarios(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM usuario")
        resultados = cursor.fetchall()

        for user in resultados:
            print(user)
        cursor.close()

    def crear_usuario(self, user):
        cursor = self.mydb.cursor()
        
        sql = "INSERT INTO usuario (id_user,nombre, apellido, email, passwd, fecha_reg, id_rol, is_active)"\
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

        val=(
            user.id_user,
            user.nombre,
            user.apellido,
            user.email,
            user.passwd,
            user.fecha_reg,
            user.id_rol,
            user.is_active
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

    def eliminar_usuario (self):
        pass