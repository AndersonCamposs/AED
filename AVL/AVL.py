from Aluno import Aluno


class AVL:
    def __init__(self) -> None:
        self.root = None
    
    def height(self, subTree):
        if (subTree == None): return 0
        return 1 + max(self.height(subTree.left), self.height(subTree.right))
    
    def balancingFactor(self, subTree):
        if (subTree == None): return 0
        return self.height(subTree) - self.height(subTree)
    
    def simpleRotationRight(self, subTree):
        aux = subTree.left
        subTree.left = aux.right
        return aux # Setar com o filho à esquerda do pai
    
    def simpleRotationLeft(self, subTree):
        aux = subTree.right
        subTree.right = aux.left
        return aux
