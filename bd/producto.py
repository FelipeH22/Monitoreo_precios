import conecta

con=conecta.crea_conexion()

def get_producto(url):
    curs=con.cursor()
    curs.execute("SELECT id FROM productos WHERE url= %s",(url,))
    return curs.fetchone()

def get_precio_actual(id):
    curs = con.cursor()
    curs.execute("SELECT pri.precio FROM productos AS pr INNER JOIN precios AS pri ON pr.id = pri.id_producto WHERE pri.id= %s ORDER BY pri.fecha DESC LIMIT 1;", (id,))
    precio=str(curs.fetchone()[0]).rstrip()
    return int(precio)

def get_precios(url):
    curs = con.cursor()
    curs.execute("SELECT pri.precio FROM productos AS pr INNER JOIN precios AS pri ON pr.id = pri.id_producto WHERE url= %s ORDER BY pri.fecha DESC;", (url,))
    return [int(str(x[0]).rstrip()) for x in curs.fetchall() if x !=None]

def get_productos():
    curs = con.cursor()
    curs.execute("SELECT * FROM productos")
    resultado=curs.fetchall()
    return [x for x in resultado]

def insert_producto(nombre,tienda,url):
    curs=con.cursor()
    valores=(nombre,tienda,url)
    curs.execute("INSERT INTO productos (nombre,tienda,url) VALUES (%s,%s,%s)", valores)
    con.commit()
