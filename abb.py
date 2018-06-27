class Node:
    def __init__(self, nombre, apellido, telefono, mail):
        self.left = None
        self.right = None
        self.apellido = apellido
        self.datos = string
        self.nombre = nombre
        self.mail = mail
        self.telefono = telefono
        self.padre = None 
class abb:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root == None

    def _insert(self, value, node):
        if value > node.value:
            if node.right == None:
                node.right = Node(value)
                node.right.padre = node
            else:
                self._insert(value, node.right)
        elif value < node.value:
            if node.left == None:
                node.left = Node(value)
                node.left.padre = node
            else:
                self._insert(value, node.left)
        else:
            print("contacto ya existe")

    def insert(self, value):
        if self.empty():
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _find(self, apellido, node):
        if node == None:
            return None
        elif apellido == node.apellido:
            return node
        elif apellido < node.apellido and node.left != None:
            return self._find(apellido, node.left)
        elif apellido > node.apellido and node.right != none:
            return self._find(apellido, node.right)
    def find(self, apellido):
        if self.empty():
            return None
        else:
            return self._find(apellido, self.root)

    def delete(self, value): 
        if self.empty():
            return None
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        def min_value_node(n):
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
            successor = min_value_node(node.right) # Get the inorder successor of the deleted node
            node.value = successor.value # Copy the value
            self.delete_node(successor)