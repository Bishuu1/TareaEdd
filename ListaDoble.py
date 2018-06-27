class Node:
    def __init__(self, nombre, apellido, telefono, mail):
        self.apellido = apellido
        self.nombre = nombre
        self.mail = mail
        self.telefono = telefono
        self.next = None
        self.prev = None

class LDE:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None

    def insert_atras(self, data):
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
    def buscar (self, apellido):
        if self.empty():
            return false        
        else:
            aux = self.head
            while (false):
                if aux.apellido == apellido:
                    return aux
                    true
                elif aux == self.tail:
                    print ("contacto no encontrado")
                    return true
                else:
                    aux = aux.next 
    def eliminashon (self, apellido): //dudas con este, revisar
        if self.buscar(apellido):
            self.buscar(apellido).prev.next = self.buscar(apellido).next
            self.buscar(apellido).next.prev = self.buscar(apellido).prev



    def imprimir(self):
        if self.empty():
             print("Agenda vacia")
        else:
            temp = self.head
            i = 1
            while True:
                print("Nodo {} contiene el número {}".format(i, temp.apellido))
                temp = temp.next
                i += 1
                if temp == None:
                    break
    