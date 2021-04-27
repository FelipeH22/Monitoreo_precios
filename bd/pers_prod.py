import conecta

con=conecta.crea_conexion()

def get_pers_prod():
    curs=con.cursor()
    query="SELECT * FROM per_pro"
    curs.execute(query)
    resultados=curs.fetchall()
    return resultados