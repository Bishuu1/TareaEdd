class Node:
    def __init__(self, data):
        self.status = None
        self.data = data
        self.papi = None 
        self.left = None
        self.right = None
class avl:
    def __init__ (self):
        self.root: None
    def empty (self):
        if self.root == None:
            return true        
    def insert (self, valor):
        if self.empty():
            self.root = valor
        else:
            self._insert(valor,self.root) 
    def _insert (self,valor,node):
        if valor> node.data:
            if node.right == None:
                node.right = Node(valor)
                node.right.papi = node
        
            
