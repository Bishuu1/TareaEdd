class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.papi = None 
class BST:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root == None

    def _insert(self, value, node):
        if value > node.value:
            if node.right == None:
                node.right = Node(value)
                node.right.papi = node
            else:
                self._insert(value, node.right)
        elif value < node.value:
            if node.left == None:
                node.left = Node(value)
                node.left.papi = node
            else:
                self._insert(value, node.left)
        else:
            print("contacto ya existe")

    def insert(self, value):
        if self.empty():
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _find(self, value, node):
        if node == None:
            return None
        elif value == node.value:
            return node
        elif value < node.value and node.left != None:
            return self._find(value, node.left)
        elif value > node.value and node.right != none:
            return self._find(value, node.right)