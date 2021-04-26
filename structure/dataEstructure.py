import sys
sys.path.append('../bd')
from bd import conecta
from bd import persona

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

    def pop():
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

class Person():
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

    def show(self):
        print(str(self.id) + ' ' + str(self.name) + ' ' + str(self.password))


datostime = time()
datos = persona.get_ejemplo()
datosFin = time()-datostime

DoublyLinkedList = DoublyLinkedList()

startTime = time()

for x in datos:
    newPerson = Person(x[0], x[1], x[2])
    DoublyLinkedList.insert_at_end(newPerson)

totalTime = time()-startTime

DoublyLinkedList.print()

print("Tiempo Traida: ",datosFin)
print("Insercción: ",totalTime)


