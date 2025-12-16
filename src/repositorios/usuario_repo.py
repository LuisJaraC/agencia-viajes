class UsuarioRepo():
    def __init__(self, mydb):
        self.mydb = mydb

    def leer_usuarios(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM agencia_viajes")
        resultados = cursor.fetchall()

        for user in resultados:
            print(user)
        cursor.close()
