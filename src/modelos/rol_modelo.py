class Rol:
    def __init__(self, id_rol=None, nombre=None):
        self.id_rol = id_rol
        self.nombre = nombre

    def __str__(self):
        return f"Rol[{self.id_rol}]: {self.nombre}"