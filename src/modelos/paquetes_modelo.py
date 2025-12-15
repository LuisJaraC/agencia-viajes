from datetime import date

class Paquete:
    def __init__(self, id_paquete=None, nombre_paq=None, precio=0, cupos=0, stock=True, fecha_ini=None, fecha_fin=None, is_active=True):
        self.id_paquete = id_paquete
        self.nombre_paq = nombre_paq
        self.precio = precio
        self.cupos = cupos
        self.stock = stock
        self.fecha_ini = fecha_ini
        self.fecha_fin = fecha_fin
        self.is_active = is_active

    def __str__(self):
        estado = "Disponible" if self.stock else "Agotado"
        return f"Paquete[{self.id_paquete}]: {self.nombre_paq} (${self.precio}) - {estado}"