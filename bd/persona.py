import conecta
import base64 as codificador

con=conecta.crea_conexion()
def get_persona(correo):
    curs=con.cursor()
    curs.execute("SELECT * FROM personas WHERE correo= ?",(correo,))
    return curs.fetchone()

def get_personas():
    curs=con.cursor()
    query="SELECT top 10000000 correo,pass FROM personas"
    curs.execute(query)
    resultados=curs.fetchall()
    return resultados

def insert_persona(correo,password):
    curs=con.cursor()
    valores=(correo,codificador.b64encode(bytes(password, 'utf-8')))
    curs.execute("INSERT INTO personas (correo,pass) VALUES (?,?)", valores)
    con.commit()

def get_productos_persona(correo):
    curs = con.cursor()
    curs.execute("SELECT personas.correo, productos.nombre, precios.precio, precios.fecha FROM personas JOIN per_pro r1 ON r1.id_persona=personas.id JOIN productos ON r1.id_producto=productos.id JOIN precios ON r1.id_producto=precios.id_producto AND fecha=(SELECT MAX(fecha) FROM precios pree WHERE r1.id_producto=pree.id_producto) WHERE personas.correo= %s; ", (correo,))
    resultado=curs.fetchall()
    return resultado