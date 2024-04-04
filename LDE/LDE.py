from Produto import Produto

class LDE:
    def __init__(self) -> None:
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    def imprimir(self):
        aux = self.cabeca
        contador = 0
        if (self.cabeca == None):
            print("Lista vazia.")
            return
        while (aux.prox != None):
            print(contador, aux.nome)
            aux = aux.prox
            contador += 1
        print(contador, aux.nome)

    def imprimirInverso(self):
        aux = self.cauda
        contador = self.tamanho - 1
        if (self.cauda == None):
            print("Lista vazia.")
            return
        
        while (aux.ant != None):
            print(contador, aux.nome)
            aux = aux.ant
            contador -= 1
        print(contador, aux.nome)

    def inserirInicio(self, novoElemento):
        if (self.cabeca == None):
            self.cabeca = novoElemento
            self.cauda = novoElemento
            self.tamanho += 1

        else:
            novoElemento.prox = self.cabeca
            self.cabeca.ant = novoElemento
            self.cabeca = novoElemento
            self.tamanho += 1

    def inserirFim(self, novoElemento):
        if (self.cabeca == None):
            self.cabeca = novoElemento
            self.cauda = novoElemento
            self.tamanho += 1
        
        else:
            novoElemento.ant = self.cauda
            self.cauda.prox = novoElemento
            self.cauda = novoElemento
            self.tamanho += 1

    def inserirMeio(self, novoElemento, indice):
        aux = self.cabeca
       
        if (indice <= (self.tamanho//2)):
            aux = self.cabeca
            posicao = 0
            while (posicao < (indice - 1)):
                aux = aux.prox
                posicao += 1 
        
        else:
            aux = self.cauda
            posicao = self.tamanho - 1
            while (posicao > (indice + 1)):
                aux = aux.ant
                posicao -= 1

        novoElemento.prox = aux.prox
        aux.prox = novoElemento
        novoElemento.ant = aux
        novoElemento.prox.ant = novoElemento
        self.tamanho += 1

    def removerFim(self):
        if (self.tamanho == 0):
            print('lista vazuia.')
        
        elif (self.tamanho == 1):
            self.cabeca = None
            self.cauda = None
            tamanho -= 1
        
        else:   
            aux = self.cauda.ant
            self.cauda.ant = None
            self.aux.prox = None
            self.cauda = aux
            self.tamanho -= 1
    
    def removerInicio(self):
        if (self.tamanho == 0):
            print("Lista vazia.")
        
        elif (self.tamanho == 1):
            self.cabeca = None
            self.cauda = None

        else:
            aux = self.cabeca.prox
            self.cabeca.prox = None
            aux.ant = None
            self.cabeca = aux

    def removerMeio(self, indice):
        if (indice == 0):
            self.removerInicio()
        
        elif (indice == self.tamanho - 1):
            self.removerFim()
        
        
        
        elif (self.tamanho == 1):
            pass
           
        else:
            aux = self.cabeca
            posicao = 0
            
            while (posicao < (indice - 1)):
                aux = aux.prox
                posicao += 1

            remover = aux.prox
            
            aux.prox = remover.prox
            aux.prox.ant = aux
            remover.prox.prox = None
            remover.prox.ant  = None 
            self.tamanho -= 1   


        
lista = LDE()

coca = Produto("Coca")
biscoito = Produto("Biscoito")
pao = Produto("Pão")
sabao = Produto("Sabão")
lista.inserirInicio(coca)
lista.inserirInicio(biscoito)
lista.inserirFim(pao)

lista.imprimir()
print("\n\n----------------------------------------------\n\n")

lista.inserirMeio(sabao, 1)
lista.imprimir()
print("\n")
#lista.imprimirInverso()
lista.removerMeio(1)
print("\n")
lista.imprimir()

'''print("\n\n",sabao.ant.nome)
print("\n\n",sabao.prox.nome)'''

