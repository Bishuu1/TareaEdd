class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LDE:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None

    def insertar_por_atras1313(self, data):
        if self.empty():
            self.head = Node(data)
            self.tail = self.head
        else:
            node  = Node(data)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def insert_adelante(self, data):
        if self.empty():
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data)
            node.next = self.head
            self.head.prev = node
            self.head = node

    def imprimir(self):
        if self.empty():
             print("Agenda vacia")
        else:
            temp = self.head
            i = 1
            while True:
                print("Nodo {} contiene el número {}".format(i, temp.value))
                temp = temp.next
                i += 1
                if temp == None:
                    break
    