from Aluno import Aluno


class AVL:
    def __init__(self) -> None:
        self.root = None
    
    def height(self, subTree):
        if (subTree == None): return 0
        return 1 + max(self.height(subTree.left), self.height(subTree.right))
    
    def balancingFactor(self, subTree):
        if (subTree == None): return 0
        return self.height(subTree.left) - self.height(subTree.right)
    
    def simpleRotationRight(self, subTree):
        aux = subTree.left
        subTree.left = aux.right
        aux.right = subTree
        return aux # Setar com o filho à esquerda do pai
    
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

    def insert(self, newElement, subTree):
        if (subTree == None):
            self.root = newElement
            return self.root
        
        if (newElement.id <= subTree.id):
            if (subTree.left != None):
                self.insert(newElement, subTree.left)
            else: 
                subTree.left = newElement
                return newElement
        
        fb = self.balancingFactor(subTree)
        if (fb > 1 or fb < -1):
            if (fb > 1):
                print("Simple Rotation Right of node", subTree.id)
                nodeTopOfRotation = self.simpleRotationRight(subTree)
                if (nodeTopOfRotation.right == self.root):
                    self.root = nodeTopOfRotation
            if (fb < -1):
                print("Simple Rotation Left of node", subTree.id)
                nodeTopOfRotation = self.simpleRotationLeft(subTree)
                if (nodeTopOfRotation.left == self.root):
                    self.root = nodeTopOfRotation




avl = AVL()

a1 = Aluno(50)
a2 = Aluno(25)
a3 = Aluno(10)

avl.insert(a1, avl.root)
avl.insert(a2, avl.root)
avl.insert(a3, avl.root)

avl.printPreOrder(avl.root)
