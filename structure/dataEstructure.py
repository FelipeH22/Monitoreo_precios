import sys
sys.path.append('../bd')
from bd import conecta
from bd import persona
from bd import producto
from bd import precio
from bd import pers_prod
from time import  time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            self.tail = node
            print("node inserted")
            return
        node = Node(data)
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            self.tail = node
            print("node inserted")
            return
        node = Node(data)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def insert_after_item(self, x, data):
        if self.head is None:
            print("List is empty")
            return
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.next
            if n is None:
                print("item not in the list")
            else:
                node = Node(data)
                node.prev = n
                node.next = n.next
                if n.next is not None:
                    n.next.prev = node
                else:
                    self.tail = node
                n.next = node

    def delete_at_start(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def delete_element_by_value(self, x):
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head.next is None:
            if self.head.data == x:
                self.head = None
                self.tail = None
            else:
                print("Item not found")
            return

        if self.head.data == x:
            self.head = self.head.next
            self.head.prev = None
            return
        n = self.head
        while n.next is not None:
            if n.data == x:
                break
            n = n.next
        if n.next is not None:
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            if n.data == x:
                self.tail = n.prev
                self.tail.next = None
            else:
                print("Element not found")

    def print_recursive(self):
        print("List Recursive: ")
        self.print_r(self.head)
        print()

    def print_r(self, node):
        if (node is not None):
            node.data.print()
            self.print_r(node.next)

    def print(self):
        print('List: ')
        start = self.head
        while start:
            print(start.data.show())
            start = start.next

class Stack:

    def __init__(self):
        self.top = None

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.empty():
            print("The stack has no element to pop")
            node = Node(None)
            return node
        else:
            node = self.top
            self.top = self.top.next
            return node

    def empty(self):
        if self.top is None:
            return True
        else:
            return False

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
        print(str(self.id)+' '+str(+self.nombre)+' '+str(self.tienda)+' '+str(self.url))

class price():
    def __init__(self, id, precio, fecha, id_producto):
        self.id=id
        self.precio=precio
        self.fecha=fecha
        self.id_producto=id_producto

    def show(self):
        print(str(self.id)+" "+str(+self.precio)+" "+str(self.fecha)+" "+str(self.id_producto))

class per_pro():
    def __init__(self,id_persona,id_producto):
        self.id_persona=id_persona
        self.id_producto=id_producto
    def show(self):
        print(str(self.id_persona)+" "+str(+self.id_producto))

datostime = time()
datos_persona=persona.get_personas()
datos_producto=producto.get_productos()
datos_precios=precio.get_precios()
datos_pers_prod=pers_prod.get_pers_prod()

datosFin = time()-datostime

lista_personas=DoublyLinkedList()
lista_productos=DoublyLinkedList()
lista_precios=DoublyLinkedList()
lista_per_pro=DoublyLinkedList()

startTime = time()

for x in datos_persona:
    newPerson = person(x[0], x[1], x[2])
    lista_personas.insert_at_end(newPerson)
for x in datos_producto:
    newPerson = product(x[0], x[1], x[2],x[3])
    lista_personas.insert_at_end(newPerson)
for x in datos_precios:
    newPerson = price(x[0], x[1], x[2],x[3])
    lista_personas.insert_at_end(newPerson)
for x in datos_pers_prod:
    newPerson = per_pro(x[0], x[1])
    lista_personas.insert_at_end(newPerson)


totalTime = time()-startTime
lista_personas.print()
lista_productos.print()
lista_precios.print()
lista_per_pro.print()

print("Tiempo Traida: ",datosFin)
print("Insercción: ",totalTime)


