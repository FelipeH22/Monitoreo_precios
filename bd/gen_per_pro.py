import conecta
import random

con=conecta.crea_conexion()
def insert_per_pro(id_persona,id_producto):
    curs=con.cursor()
    valores=(id_persona,id_producto)
    curs.execute("INSERT INTO per_pro (id_persona,id_producto) VALUES (%s,%s)", valores)
    con.commit()

for a in range(0,500000):
    try:
        insert_per_pro(random.randint(1,45568),random.randint(1,30))
        print("se ha añadido el registo",a)
    except: print("No se puede insertar. Está añadiendo un producto a una persona que ya lo tenía")
