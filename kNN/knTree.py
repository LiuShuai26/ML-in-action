import operator

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class KnTree:
    def __init__(self):
        self.root = None
        self.k = None

    def buildTree(self, data, n, k):
        l = len(data)
        if l == 0:
            return None
        F = sorted(data, key=operator.itemgetter(n))
        mid = int(l/2)
        node = Node(F[mid])
        node.l = self.buildTree(data[:mid], (n+1) % k, k)
        node.r = self.buildTree(data[mid+1:], (n+1) % k, k)
        return node


    def getk(self, data):
        self.k = len(data[0])

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val is node.v:
            return node
        elif val < node.v and node.l:
            self._find(val, node.l)
        elif val > node.v and node.r:
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if self.root:
            self._printTree(self.root)

    def _printTree(self, node):
        if node:
            self._printTree(node.l)
            print(str(node.v) + ' ', end='')
            self._printTree(node.r)


T = [[2, 3, 1], [5, 4, 8], [9, 6, 5], [4, 7, 9], [8, 1, 4], [7, 2, 3]]

kntree = KnTree()
kntree.root = kntree.buildTree(T, 0, 2)
kntree.printTree()
