import conecta
from datetime import datetime
from ws import WS
import producto

con=conecta.crea_conexion()
def insert_precio(precio,id_producto):
    curs=con.cursor()
    fecha=datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    valores=(precio,fecha,id_producto)
    curs.execute("INSERT INTO precios (precio,fecha,id_producto) VALUES (?,?,?)", valores)
    con.commit()

def get_producto(url):
    curs=con.cursor()
    curs.execute("SELECT id FROM productos WHERE url= ?",(url,))
    return curs.fetchone()


archivo=open("../links_pruebas.txt").read()
archivo=archivo.split("\n")
for link in archivo:
    print(link)
    contador=int(get_producto(link)[0])
    print(contador)
    try:
        precio=int("".join(WS.get_producto(link).split(".")))
        id_pr=int(contador)
        print(precio,contador)
        insert_precio(precio,contador)
        print("Sí se pudo")
        contador+=1
    except Exception as e: print("No se pudo",e)
