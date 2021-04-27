import pyodbc

def crea_conexion():
    direccion_servidor = 'monitoreop.database.windows.net'
    nombre_bd = 'monitoreo_precios'
    nombre_usuario = 'user'
    password = 'colombia$2021'
    try:
        conexion=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                  direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
        return conexion
    except Exception as e:
        print("Ocurrió un error al conectar a SQL Server: ", e)
