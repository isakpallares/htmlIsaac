import sqlite3


def conectar_db(nombre_db):
    try:
        conexion = sqlite3.Connection(nombre_db)
        cursor = conexion.cursor()
        return conexion, cursor
        
    except sqlite3.Error as error:
        print('Error al abrir la base de datos:', error)
        return None, None
        
def desconectar_db(conexion, cursor):
    if conexion:
        cursor.close()
        conexion.close()
        print("La conexión con la base de datos ha sido cerrada correctamente.")
    
    