import textwrap

class ReservaVista():
    def __init__(self):
        pass

    def tomar_datos_reserva(self, paquetes_disponibles):  
        while True:
            print("\n      Selecciona paquete para ver detalles \n")
            for i, paquete in enumerate(paquetes_disponibles):
                print(f'{i+1}. {paquete[1]}')
            print("0. Para volver")

            try:
                eleccion = input("Eleccion: ")

                if not eleccion.isdigit():
                    print("Ingrese un numero valido")
                    continue

                entrada = int(eleccion)

                if entrada == 0:
                    # usuario quiere volver atras
                    return None
                
                indice_real = entrada - 1

                if 0 <= indice_real < len(paquetes_disponibles):
                    paquete_elegido = paquetes_disponibles[indice_real]

                    mensaje =f"""
                        1. Nombre: {paquete_elegido[1]} 
                        2. Precio por persona: {paquete_elegido[2]}
                        3. Cupos disponibles: {paquete_elegido[3]}
                        4. Fecha inicio: {paquete_elegido[4]}
                        5. Fecha fin: {paquete_elegido[5]}
                    """
                    print(textwrap.dedent(mensaje))
                    
                    confirmacion = input("""1. Confirmacion \n2. Ver otro paquete \nEleccion: """)
                    
                    if confirmacion == "2":
                        continue
                    elif confirmacion == "1":
                        cant_str = input("Ingrese cantidad de cupos: ")
                        if cant_str.isdigit():
                            # retorna tupla y un int
                            return (paquete_elegido, int(cant_str))
                        else:
                            print("Cantidad inválida.")
                else:
                    print("Opcion fuera de rango") 
            except Exception as e:
                print(f"Ocurrió un error: {e}")     

    def confirmar_monto(self, monto):
        confirmacion = None
        if monto == None:
            print("\nNo hay cupos suficientes")
        else:
            confirmacion = input(f""" Monto total: {monto}
                                    1. Confirmar reserva
                                    2. Declinar reserva""")
        
        return confirmacion