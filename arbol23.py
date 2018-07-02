class node:
    def  __init__ ( self , nombre, apellido, telefono, mail ):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail = mail
        self.hijo = []
        self.padre =  None

 class Arbol:
    def  __init__ (self):
        self.raiz = None

    def hoja( self ):
        return  len(self.hijo) ==  0
    
    def  agregar ( self , nombre, apellido, telefono, mail ):
        for hijo in node(nombre, apellido, telefono, mail).hijo:
            hijo.padre =  self
        self.hijo.extend (node(nombre, apellido, telefono, mail).child)
       
        if len (self.hijo) > 1 :
        	self.hijo.sort ()
        if len (self.data) >  2 :
            self.Dividir ()

    def Insertar ( self ,nombre, apellido, telefono, mail ):
        if  self.hoja ():
            self.agregar(node(nombre, apellido, telefono, mail))
        elif node(nombre, apellido, telefono, mail).data [ 0 ] >  self.data [ - 1 ]:
            self.hijo [- 1].Insertar(node(nombre, apellido, telefono, mail))
        else :
            for i in range ( 0 , len ( self.data)):
                if node(nombre, apellido, telefono, mail).data [ 0 ] < self .data [i]:
                    self .child [i].Insertar(node(nombre, apellido, telefono, mail))
                    break
    
    def Dividir ( self ):
        HijoIzq = Node ( self.data[0], self )
        HijoDer = Node ( self.data[2], self )
            if self.hijo:
        	self .hijo [ 0 ] .padre = HijoIzq
        	self .hijo [ 1 ] .padre = HijoIzq
        	self .hijo [ 2 ] .padre = HijoDer
        	self .hijo [ 3 ] .padre = HijoDer
        	HijoIzq.hijo = [self.hijo[0], self.hijo[1]]
            HijoDer.hijo = [self.hijo[2], self.hijo[3]]

        self.hijo = [HijoIzq]
        self.hijo.append (HijoDer)
        self.data = [self.data[1]]

        if self.padre:
        	if self in self.padre.hijo:
        		self.padre.hijo._remove(self)
        	self.padre._add(self)
        else :
        	HijoIzq.padre = self
            HijoDer.padre = self

    def  buscar( self, elemento ):
    	if elemento in self.data
    		return elemento
    	elif  self.hoja():
    		return False
    	elif elemento>self.data [-1]:
    		return  self.hijo[-1].buscar(elemento)

    	else :
    		for i in range(len(self.data)):
                if elemento < self .data [i]:
    				return self.hijo[i]._find(elemento)

    def  eliminar( self, elemento ):
    	pasar

    def  EnOrden(self):
    	print(self)
    	for hijo in self.hijo
            child._EnOrden()

   
   def  Vacio (self):
        return  self.raiz ==  None

        def  insertar ( self , valor ):
        if  self .Vacio():
            self.raiz= Node (valor)
        else :
            self .raiz._insertar(Node(valor))
            while  self.raiz.padre:
                self.raiz = self.raiz.padre
                    return True

    def  remove ( auto , elemento ):
        pasar

    def  find ( auto , elemento ):
        return  self.root._encontrar(elemento)

    
 