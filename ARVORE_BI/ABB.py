class ABB:
    def __init__(self) -> None:
        self.root
    
    def inserir(self, subArvore, newElement):
        # se a árvore estiver vazia
        if (self.root == None):
            self.root = newElement
            return
        # árvore não vazia
        if (subArvore > newElement.content):
            if (subArvore.left == None):
                self.root.left = newElement
            else:
                self.inserir(subArvore, newElement)
        
