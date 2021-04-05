import conecta
import base64 as codificador

con=conecta.crea_conexion()
def get_persona(correo):
    curs=con.cursor()
    curs.execute("SELECT * FROM personas WHERE correo= %s",(correo,))
    return curs.fetchone()

def get_personas():
    curs=con.cursor()
    curs.execute("SELECT * FROM personas")
    resultados=curs.fetchall()
    for x in resultados: print(x)

def insert_persona(correo,password):
    curs=con.cursor()
    valores=(correo,codificador.b64encode(bytes(password, 'utf-8')))
    curs.execute("INSERT INTO personas (correo,pass) VALUES (%s,%s)", valores)
    con.commit()

insert_persona("juherrera5@gmail.com","holamuybuenastardes$4567")
print(get_personas())
