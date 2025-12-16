class RolRepo():
    def __init__(self, mydb):
        self.mydb = mydb

    def leer_rol(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM rol")
        resultados = cursor.fetchall()

        for rol in resultados:
            print(rol)
        cursor.close()

