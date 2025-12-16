import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

#sello para encriptar datos sensibles (TOKEN)
secret_key = os.getenv('secret_key')

class Conexion:
    def __init__(self):
        #se inicializa en None como una caja vacia para que no se rompa el programa
        self.mydb = None

        #se inicializan asi para que se guarden en memoria y poder verificar la conexion por medio de los print del main
        #por seguridad solo se guarda en memoria el host para saber que se hizo una conexion
        self.host = os.getenv('host')
        
        try:
            self.mydb = mysql.connector.connect(
                host = self.host, 
                user = os.getenv('user'),
                password= os.getenv('password'),
                database =os.getenv('database')
            )
        except mysql.connector.Error as e:
            print(f"Error de conexion {e}")
    
    def get_conexion(self):
        return self.mydb
