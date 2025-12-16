class DestinoPaquete:
    def __init__(self, id_dest_paq=None, id_destino=None, id_paquete=None):
        self.id_dest_paq = id_dest_paq
        self.id_destino = id_destino
        self.id_paquete = id_paquete

    def __str__(self):
        return f"Destino Paquete[{self.id_dest_paq}]: {self.id_destino} {self.id_paquete}"