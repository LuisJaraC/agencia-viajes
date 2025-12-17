from datetime import datetime

class Usuario:
    def __init__(self, id_user=None, nombre=None, apellido=None, email=None, passwd=None, id_rol=None, fecha_reg=None, is_active=True):
        self.id_user = id_user
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.passwd = passwd
        self.fecha_reg = fecha_reg or datetime.now()
        self.id_rol = id_rol
        self.is_active = is_active

    def __str__(self):
        return f"Usuario[{self.id_user}]: {self.nombre} {self.apellido} ({self.email})"