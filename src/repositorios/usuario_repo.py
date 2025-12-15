class UsuarioRepo():
    def __init__(self, mydb):
        self.mydb = mydb

    def leer_usuarios(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM veterinario")
        resultados = cursor.fetchall()

        for vet in resultados:
            print(vet)
        cursor.close()
