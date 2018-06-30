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
        self.n = 0

    def empty(self):
        return self.head == None

    def insert_atras(self, nombre, apellido, telefono, mail):
        if self.empty():
            self.head = Node(nombre, apellido, telefono, mail)
            self.tail = self.head
        else:
            node  = Node(nombre, apellido, telefono, mail)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        n++

    def insert_adelante(self, nombre, apellido, telefono, mail):
        if self.empty():
            self.head = Node(nombre, apellido, telefono, mail)
            self.tail = self.head
        else:
            node = Node(nombre, apellido, telefono, mail)
            node.next = self.head
            self.head.prev = node
            self.head = node
        n++
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
        if self.buscar(apellido) == self.head:
            self.head.next.prev = None
            self.head = self.head.next
        if self.buscar(apellido) == self.tail:
            self.tail.prev.next = None
            self.tail = self.tail.prev
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
                print("Datos: ".format(i, temp.nombre, temp.apellido, temp.telefono, temp.email))
                temp = temp.next
                i += 1
                if temp == None:
                    break
       
    