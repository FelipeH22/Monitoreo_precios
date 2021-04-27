import conecta

con=conecta.crea_conexion()

def get_precios():
    curs=con.cursor()
    query="SELECT * FROM precios"
    curs.execute(query)
    resultados=curs.fetchall()
    return resultados