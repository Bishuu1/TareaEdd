class node:
    def __init__(self, nombre, apellido, telefono, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.telefono = telefono 
        self.right = None
        self.left = None

class arbol_avl():
    def __init__(self):
        self.root = None 
        self.altura = -1  
        self.balance = 0
    
    def insertar(self, nombre, apellido, telefono, mail):                   
        tree = self.root 
        if tree == None:
            self.root = node(nombre, apellido, telefono, mail) 
            self.root.left = arbol_avl() 
            self.root.right = arbol_avl()
        
        elif apellido[0] > tree.apellido[0]: 
            self.root.right.insertar(nombre,apellido,telefono,mail)
            
        else: 
            self.root.left.insertar(nombre,apellido,telefono,mail)
        self.rebalancear() 
        
    def rebalancear(self):
        self.update_alturas(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.root.left.balance < 0:  
                    self.root.left.left_rotate()
                    self.update_alturas()
                    self.update_balances()
                self.right_rotate()
                self.update_alturas()
                self.update_balances()
                
            if self.balance < -1:
                if self.root.right.balance > 0:  
                    self.root.right.right_rotate()
                    self.update_alturas()
                    self.update_balances()
                self.left_rotate()
                self.update_alturas()
                self.update_balances()


            
    def right_rotate(self): 
        base = self.root 
        izq = self.root.left.root 
        der = izq.right.root 
        self.root = izq 
        izq.right.root = base
        base.left.root = der 

    
    def left_rotate(self):
        base = self.root 
        der = self.root.right.root 
        izq = der.left.root 
        self.root = der 
        der.left.root = base 
        base.right.root = izq 
        
            
    def update_alturas(self, recurse=True):
        if not self.root == None: 
            if recurse: 
                if self.root.left != None: 
                    self.root.left.update_alturas()
                if self.root.right != None:
                    self.root.right.update_alturas()
            
            self.altura = max(self.root.left.altura,
                              self.root.right.altura) + 1 
        else: 
            self.altura = -1 
            
    def update_balances(self, recurse=True):
        if not self.root == None: 
            if recurse: 
                if self.root.left != None: 
                    self.root.left.update_balances()
                if self.root.right != None:
                    self.root.right.update_balances()

            self.balance = self.root.left.altura - self.root.right.altura 
        else: 
            self.balance = 0 

    def eliminar(self, value):                                                   
        if self.root != None: 
            if self.root.apellido == value: 
                if self.root.left.root == None and self.root.right.root == None:  
                    self.root = None  
                elif self.root.left.root == None: 
                    self.root = self.root.right.root
                elif self.root.right.root == None: 
                    self.root = self.root.left.root
                else:  
                    replacement = self.sucesor(self.root)
                    if replacement != None:
                        self.root.apellido(replacement.apellido)  
                        self.root.right.eliminar(replacement.apellido)              
                self.rebalancear()
                return  
            elif value <= self.root.apellido: 
                self.root.left.eliminar(value)  
            elif value > self.root.apellido: 
                self.root.right.eliminar(value)
                        
            self.rebalancear()
        else: 
            return 
    
    def sucesor(self, aux):
        aux = aux.right.root  
        if aux != None:
            while aux.left != None:
                if aux.left.root == None: 
                    return aux 
                else: 
                    aux = aux.left.root  
        return aux 


    def buscar(self,value):                                                          
        if(self.root != None):
            if self.root.apellido == value:
                print(True)
                return True
            self.root.left.buscar(value)
            self.root.right.buscar(value)
        return
    
    def imprimir_in_order(self, node): 
        if node==None:
            return None
        else:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)
    