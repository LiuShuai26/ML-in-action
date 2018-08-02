import operator


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val



class Tree:
    def __init__(self):
        self.root = None

    def buildTree(self, data):
        l = len(data)
        if l == 0:
            return None
        mid = int(l/2)
        node = Node(data[mid])
        node.l = self.buildTree(data[:mid])
        node.r = self.buildTree(data[mid+1:])
        return node

    def printTree(self):
        if self.root is None:
            return
        else:
            self._printTree(self.root)

    def _printTree(self, node):
        if node:
            self._printTree(node.l)
            print(node.v)
            self._printTree(node.r)


t = Tree()

data = [1, 2, 3, 4, 5, 6]

t.root = t.buildTree(data)
t.printTree()
