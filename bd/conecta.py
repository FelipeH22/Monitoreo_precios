import mysql.connector as connector

def crea_conexion():
    config={
        "user": "root",
        "password": "toor",
        "host": "localhost",
        "database": "monitoreo_precios"
    }
    try:
        c = connector.connect(**config)
        return c
    except:
        print("error en la conexión")

