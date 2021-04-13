import conecta
import random
from datetime import datetime
from ws import WS
import producto

con=conecta.crea_conexion()
def insert_precio(precio,id_producto):
    curs=con.cursor()
    fecha=datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    valores=(precio,fecha,id_producto)
    curs.execute("INSERT INTO precios (precio,fecha,id_producto) VALUES (%s,%s,%s)", valores)
    con.commit()

for _ in range(1,201):
    id_pr=random.randint(1,30)
    promocion=random.randint(0,99999)
    precio=producto.get_precio_actual(id_pr)
    precio+=50000
    if precio-promocion>precio/2:
        precio=precio-promocion
    else:
        precio=precio+50000
    try:
        insert_precio(precio,id_pr)
        print("se ha añadido el registo",id_pr, precio)
    except Exception as e: print("No se puede insertar",e)



""" 
                        INSERTAR PRECIOS REALES EN ESTE MOMENTO
                        
archivo=open("../links_pruebas.txt").read()
archivo=archivo.split("\n")
for link in archivo:
    precio=int("".join(WS.get_producto(link).split(".")))
    id_pr=int(producto.get_producto(link)[0])
    print(precio,id_pr)
    try:
        insert_precio(precio,id_pr)
        print("Sí se pudo")
    except Exception as e: print("No se pudo",e)"""