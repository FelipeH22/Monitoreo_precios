from double_linked_list import DoublyLinkedList
import sys
sys.path.append('../bd')
from bd import persona,producto,precio,pers_prod
from time import time


class person():
    def __init__(self, id, correo, password):
        self.id = id
        self.correo = correo
        self.password = password

    def show(self):
        print(str(self.id) + ' ' + str(self.correo) + ' ' + str(self.password))

class product():
    def __init__(self, id, nombre, tienda, url):
        self.id=id
        self.nombre=nombre
        self.tienda=tienda
        self.url=url

    def show(self):
        print(str(self.id)+' '+str(self.nombre)+' '+str(self.tienda)+' '+str(self.url))

class price():
    def __init__(self, id, precio, fecha, id_producto):
        self.id=id
        self.precio=precio
        self.fecha=fecha
        self.id_producto=id_producto

    def show(self):
        print(str(self.id)+" "+str(self.precio)+" "+str(self.fecha)+" "+str(self.id_producto))

class per_pro():
    def __init__(self,id_persona,id_producto):
        self.id_persona=id_persona
        self.id_producto=id_producto
    def show(self):
        print(str(self.id_persona)+" "+str(self.id_producto))

print("Trayendo datos de la BD")
datos_persona=persona.get_personas()
datos_producto=producto.get_productos()
datos_precios=precio.get_precios()
datos_pers_prod=pers_prod.get_pers_prod()

lista_personas=DoublyLinkedList()
lista_productos=DoublyLinkedList()
lista_precios=DoublyLinkedList()
lista_per_pro=DoublyLinkedList()



def genera_linked_list():
    print("Generando listas enlazadas")
    startTime = time()
    for x in datos_persona:
        newPerson = person(x[0], x[1], x[2])
        lista_personas.insert_at_end(newPerson)
    tiempo_personas=time()-startTime

    startTime = time()
    for x in datos_producto:
        newProduct = product(x[0], x[1], x[2],x[3])
        lista_personas.insert_at_end(newProduct)
    tiempo_productos=time()-startTime

    startTime = time()
    for x in datos_precios:
        newPrice = price(x[0], x[1], x[2],x[3])
        lista_personas.insert_at_end(newPrice)
    tiempo_precios=time()-startTime

    startTime = time()
    for x in datos_pers_prod:
        newPer_Pro = per_pro(x[0], x[1])
        lista_personas.insert_at_end(newPer_Pro)
    tiempo_per_pro=time()-startTime
    print(f"Tiempo de creación de la lista enlazada personas: {tiempo_personas} ({len(datos_persona)} datos), lista productos: {tiempo_productos} ({len(datos_producto)} datos)")
    print(f"Tiempo de creación de la lista enlazada precios: {tiempo_precios} ({len(datos_precios)} datos), lista relación productos-personas {tiempo_per_pro} ({len(datos_pers_prod)} datos)")

def genera_arrays():
    print("Generando arreglos")
    personasarr=[None]*len(datos_persona)
    productosarr=[None]*len(datos_producto)
    preciosarr=[None]*len(datos_precios)
    per_pro_arr=[None]*len(datos_pers_prod)

    startTime = time()
    for x in range(len(datos_persona)):
        newPerson=person(datos_persona[x][0], datos_persona[x][1], datos_persona[x][2])
        personasarr[x]=newPerson
    tiempo_personas = time()-startTime

    startTime = time()
    for x in range(len(datos_producto)):
        newProduct=product(datos_producto[x][0], datos_producto[x][1], datos_producto[x][2], datos_producto[x][3])
        productosarr[x]=newProduct
    tiempo_productos = time()-startTime

    startTime = time()
    for x in range(len(datos_precios)):
        newPrice=price(datos_precios[x][0], datos_precios[x][1], datos_precios[x][2], datos_precios[x][3])
        preciosarr[x]=newPrice
    tiempo_precios = time()-startTime

    startTime = time()
    for x in range(len(datos_pers_prod)):
        newPers_Pro=per_pro(datos_pers_prod[x][0], datos_pers_prod[x][1])
        per_pro_arr[x]=newPers_Pro
    tiempo_per_pro=time()-startTime

    print(f"Tiempo de creación de el array personas: {tiempo_personas} ({len(datos_persona)} datos), array productos: {tiempo_productos} ({len(datos_producto)} datos)")
    print(f"Tiempo de creación de el array precios: {tiempo_precios} ({len(datos_precios)} datos), array productos-personas {tiempo_per_pro} ({len(datos_pers_prod)} datos)")


genera_linked_list()
genera_arrays()
#lista_personas.print()
#lista_productos.print()
#lista_precios.print()
#lista_per_pro.print()




