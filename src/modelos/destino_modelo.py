class Destino:
    def __init__(self, id_destino=None, nombre=None, descripcion=None, precio_base=0, is_active=True):
        self.id_destino = id_destino
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio_base = precio_base
        self.is_active = is_active

    def __str__(self):
        return f"Destino[{self.id_destino}]: {self.nombre} - ${self.precio_base}"