import conecta

con=conecta.crea_conexion()

def get_precios():
    curs=con.cursor()
    query="SELECT * FROM precios"
    curs.execute(query)
    resultados=curs.fetchall()
    return resultados

def get_precios_producto(url):
    curs=con.cursor()
    curs.execute("SELECT top 10000 precio FROM precios join productos on precios.id_producto=productos.id where productos.url=?",(url,))
    resultados=curs.fetchall()
    return resultados