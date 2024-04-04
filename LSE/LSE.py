from LSE.Animal import Animal 

class LSE:
    def __init__(self) -> None:
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    def imprimir(self):
        aux = self.cabeca
        if (self.cabeca == None):
            print("Lista vazia.")
            return
        while (aux.prox != None):
            print(aux.nome)
            aux = aux.prox
        print(aux.nome)

    def adicionarInicio(self, novoElemento):
        novoElemento.prox = self.cabeca # o novoElemento elemento aponta pra o "antigo primeiro"
        if (self.cabeca == None):
            self.cauda = novoElemento
        self.cabeca = novoElemento # o "novoElemento primeiro" passa a ser o novoElemento elemento
        self.tamanho += 1
        
    def adicionarMeio(self, novoElemento, indice):
        # add no indice 0 é o mesmo que adicionar no início
        if (indice == 0 ):
            self.adicionarInicio(novoElemento)
        # condição de qualquer indice diferente de zero
        elif (indice == self.tamanho):
            self.adicionarFim(novoElemento)
        else:
            #criei uma variável aux para percorrer a lista
            aux=self.cabeca
            # variável para contar a posição
            posicao =0
            #enquanto a posicao for menor que o indice anterior
            #ao que quero adicionar, já que, precisamos apontar
            #o prox elemento do elemento anterior que irá add
            while (posicao < (indice-1)):
                #pulo
                aux=aux.prox
                posicao+=1
            
            novoElemento.prox = aux.prox
            aux.prox=novoElemento
            self.tamanho+=1#aumentando o tamnho da lista depois de add
            
    def adicionarFim(self, novoElemento):
        self.cauda.prox = novoElemento
        self.cauda = novoElemento
        self.tamanho+=1#aumentando o tamnho da lista depois de add
        
    def removerInicio(self):
        aux=self.cabeca
        self.cabeca=aux.prox # seria a mesma coisa de 
        #self.cabeca = self.cabeca.prox
        aux.prox = None
        self.tamanho-=1#aumentando o tamnho da lista depois de add

    def removerFim(self):
        aux = self.cabeca
        while (aux.prox.prox != None):
            aux = aux.prox
        aux.prox = None
        self.cauda = aux
        self.tamanho -= 1

    def removerMeio(self, indice):
        if (indice == 0):
            self.removerInicio()
        elif (indice == self.tamanho - 1):
            self.removerFim()
        elif (indice >= self.tamanho):
            print(f"O índice {indice} é inválido.")
        else:
            aux = self.cabeca
            posicao = 0
            while (posicao < (indice - 1)):
                aux = aux.prox
                posicao += 1

            rem = aux.prox
            aux.prox = aux.prox.prox
            rem.prox = None
            self.tamanho -= 1
            


    def getTamanho(self):
        return self.tamanho 



listaDeAnimais = LSE()
peixe = Animal("Tilápia")
gato = Animal("Gato")
leao = Animal("Leão")
passaro = Animal("Pássaro")
macaco = Animal("Macaco")
tubarao = Animal("Tubarao")

listaDeAnimais.adicionarInicio(leao)
listaDeAnimais.adicionarInicio(gato)
listaDeAnimais.adicionarInicio(peixe)
listaDeAnimais.adicionarMeio(passaro,3)
listaDeAnimais.adicionarFim(macaco)
listaDeAnimais.adicionarFim(tubarao)

listaDeAnimais.imprimir()

print ("O tamanho é: ", listaDeAnimais.getTamanho())

print ("------------------")
listaDeAnimais.removerMeio(2)
listaDeAnimais.imprimir()
print ("O tamanho é: ", listaDeAnimais.getTamanho())
