class Node:
    def_init_(self, value)
        self.data=[value]
        self.parent= None
        self.childrens =[]
class arbol23:
    def _insert(self, new_node)
        if len(self.childrens)== 0;
            self._add(new_node)
        elif new_node.data[0]> self.data[-1]:
                self.childrens[-1]._insert(new_node)
        else
            for i in range(0, len(self.data))
                if new_node.data[0]< self.data[i]:
                    self.childrens[i]._insert(new_node)
                        break