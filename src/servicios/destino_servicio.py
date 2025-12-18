from ..modelos.destino_modelo import Destino

class DestinoServicio():
    def __init__(self, repo_central):
        self.repo_central = repo_central
    def leer_todos_los_destinos(self):
        return self.repo_central.DestinoRepo.leer_todos()
    def leer_destino(self):
        return self.repo_central.DestinoRepo.leer_destino()
    def crear_destino(self,destino):
        #recibe una tupla y no un objeto, por tanto hay que pasarlo a objeto
        nombre=destino[0]
        descripcion=destino[1]
        precio=destino[2]
        #paso de tupla a objeto
        lista_objeto = Destino(
            nombre=nombre,
            descripcion=descripcion,
            precio_base=precio
        )
        return self.repo_central.DestinoRepo.crear_destino(lista_objeto)
    def actualizar_destino(self,recibido_vista):
        id_destino=recibido_vista[0]
        campo=recibido_vista[1]
        dato=recibido_vista[2]

        #validacion para evitar SQL inyection
        campos_validos = ["nombre", "descripcion", "precio_base", "is_active"]
        if campo not in campos_validos:
            print(f"Error: intento de modificar {campo} no permitido")
            return False
        return self.repo_central.DestinoRepo.actualizar_destino(id_destino,campo,dato)
    def cambiar_estado(self,id_destino):
        return self.repo_central.DestinoRepo.cambiar_estado(id_destino)