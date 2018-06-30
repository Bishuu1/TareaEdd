class Node:
    def __init__(self, nombre, apellido, telefono, mail):
        self.left = None
        self.right = None
        self.apellido = apellido
        self.nombre = nombre
        self.mail = mail
        self.telefono = telefono
        self.padre = None 
class abb:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root == None

    def _insert(self, nombre, apellido, telefono, mail, node):
        if apellido[0] > node.apellido[0]:
            if node.right == None:
                node.right = Node(nombre, apellido, telefono, mail)
                node.right.padre = node
            else:
                self._insert(nombre, apellido, telefono, mail, node.right)
        elif apellido[0] < node.apellido[0]:
            if node.left == None:
                node.left = Node(nombre, apellido, telefono, mail)
                node.left.padre = node
            else:
                self._insert(nombre, apellido, telefono, mail, node.left)
        else:
            print("contacto ya existe")

    def insert(self, nombre, apellido, telefono, mail):
        if self.empty():
            self.root = Node(nombre, apellido, telefono, mail)
        else:
            self._insert(nombre,apellido,telefono,mail, self.root)

    def _find(self, apellido, node):
        if node == None:
            return None
        elif apellido == node.apellido:
            return node
        elif apellido[0] < node.apellido[0] and node.left != None:
            return self._find(apellido, node.left)
        elif apellido[0] > node.apellido[0] and node.right != none:
            return self._find(apellido, node.right)
    def find(self, apellido):
        if self.empty():
            return None
        else:
            return self._find(apellido, self.root)

    def delete(self, apellido): 
        if self.empty():
            return None
        return self.delete_node(self.find(apellido))

    def delete_node(self, node):
        def min_apellido_node(n):
            current = n
            while current.left != None:
                current = current.left
            return current
        def number_children(n): 
            number_children = 0
            if n.left != None:
                number_children += 1
            if n.right != None:
                number_children += 1
            return number_children

        node_parent = node.parent 
        node_children = number_children(node)

        # Case 1: Deleting a node without childrens
        if node_children == 0:
            if node_parent.left == node:
                node_parent.left = None
            else:
                node_parent.right = None
        # Case 2: Deleting a node with one children
        if node_children == 1:
            # Get the children of the node to be deleted
            if node.left != None:
                child = node.left
            else:
                child = node.right

            # Replace the node to be deleted with its child
            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child

            # Change the parent of the child
            child.parent = node_parent
        # Case 3: Deleting a node with two childrens
        if node_children == 2:
            successor = min_apellido_node(node.right) # Get the inorder successor of the deleted node
            node.apellido = successor.apellido # Copy the apellido
            self.delete_node(successor)
    
    def imprimir_in_order(self, node): 
        if node==None:
            return None
        else:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)
    

