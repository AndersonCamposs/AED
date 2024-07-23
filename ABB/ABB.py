from No import No
class ABB:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, subArvore, newElement):
        # se a árvore estiver vazia
        if (self.root == None):
            self.root = newElement
            return
        # árvore não vazia
        if (subArvore.value > newElement.value):
            if (subArvore.left == None):
                subArvore.left = newElement
            else:
                self.insert(subArvore.left, newElement)
        else:
            if (subArvore.right == None):
                subArvore.right = newElement
            else:
                self.insert(subArvore.right, newElement)
    
    def printInOrder(self, subArvore):
        if (subArvore.left != None):
            self.printInOrder(subArvore.left)
        print(subArvore.value)
        if (subArvore.right != None):
            self.printInOrder(subArvore.right)
    
    def printPreOrder(self, subArvore):
        print(subArvore.value)
        if (subArvore.left != None):
            self.printPreOrder(subArvore.left)
        if (subArvore.right != None):
            self.printPreOrder(subArvore.right)
    
    def printPostOrder(self, subArvore):
        if (subArvore.left != None):
            self.printPosOrder(subArvore.left)
        if (subArvore.right != None):
            self.printPosOrder(subArvore.right) 
        print(subArvore.value)
    
    def search(self, subArvore, searchValue):
        # impede que a busca seja realizada em uma árvore vazia
        if (subArvore == None):
            # se chegar aqui, é  porque chegou no último nó e 
            # não encontrou o valor buscado
            return
        
        else:
            # verifica se o valor do nó atual é o buscado
            if (subArvore.value == searchValue):
                return subArvore #retorna o nó no qual o valor foi encontrado
            else: 
                # verifica se o valor buscado está na
                #  esquerda ou direita
                if (subArvore.value > searchValue):
                    return self.search(subArvore.left, searchValue)
                else:
                    return self.search(subArvore.right, searchValue)
                