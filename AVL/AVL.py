from Aluno import Aluno
from random import sample


class AVL:
    def __init__(self) -> None:
        self.root = None
    
    def height(self, subTree):
        if (subTree == None): return 0
        return 1 + max(self.height(subTree.left), self.height(subTree.right))
    
    def getBalancingFactor(self, subTree):
        if (not subTree): return 0
        return self.height(subTree.left) - self.height(subTree.right)
    
    def simpleRotationRight(self, subTree):
        aux = subTree.left
        subTree.left = aux.right
        aux.right = subTree
        return aux
    
    def simpleRotationLeft(self, subTree):
        aux = subTree.right
        subTree.right = aux.left
        aux.left = subTree
        return aux

    def printPreOrder(self, subTree):
        print(subTree.id)
        if (subTree.left != None):
            self.printPreOrder(subTree.left)
        if (subTree.right != None):
            self.printPreOrder(subTree.right)

    def insert(self, newElement):
        self.root = self._insert(newElement, self.root)

    def _insert(self, newElement, subTree):
        if (not subTree):
            return newElement
        

        elif (newElement.id < subTree.id):
            subTree.left = self._insert(newElement, subTree.left)
        
        else:
            subTree.right = self._insert(newElement, subTree.right)
            
        balancingFactor = self.getBalancingFactor(subTree)

        if (balancingFactor > 1 and newElement.id < subTree.left.id):
            return self.simpleRotationRight(subTree)
        
        if (balancingFactor < -1 and newElement.id > subTree.right.id):
            return self.simpleRotationLeft(subTree)
        
        if (balancingFactor > 1 and newElement.id > subTree.left.id):
            subTree.left = self.simpleRotationLeft(subTree.left)
            return self.simpleRotationRight(subTree)
        
        if (balancingFactor < -1 and newElement.id < subTree.right.id):
            subTree.right = self.simpleRotationRight(subTree.right)
            return self.simpleRotationLeft(subTree)
        
        return subTree

values = sample(range(1, 101), 15)
print(values)

avl = AVL()

for value in values:
    node = Aluno(value)
    avl.insert(node)

