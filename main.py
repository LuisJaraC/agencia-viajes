from src.conexion import Conexion
from src.repositorios.repo_central import RepoCentral
from src.controladores.controlador_central import ControladorCentral
from src.servicios.servicios_central import ServiciosCentral

# Lo que antes hicismo con controlador central es con servicios_central
def main():
    conexion = Conexion()
    mydb = conexion.get_conexion()

    repo_central = RepoCentral(mydb)
    servicio_central = ServiciosCentral(repo_central)
    app = ControladorCentral(servicio_central)
    
    app.ejecutar()

if __name__ == "__main__":
    main()
