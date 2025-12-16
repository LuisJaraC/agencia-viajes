from src.modelos.rol_modelo import Rol

class RolRepo():
    def __init__(self, mydb):
        self.mydb = mydb

    def leer_rol(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM rol")
        resultados = cursor.fetchall()

        # Convertimos tupla en una lista de objetos

        lista_objetos_rol = []
        for tupla in resultados:
            rol_obj = Rol(tupla[0], tupla[1])
            lista_objetos_rol.append(rol_obj)
            
        cursor.close()
        
        return lista_objetos_rol
