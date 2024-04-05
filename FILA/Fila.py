from Animal import Animal 

class Fila:
    def __init__(self) -> None:
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    def imprimir(self):
        aux = self.cabeca
        if (self.cabeca == None):
            print("Lista vazia.")
            return
        
        contador = 0
        while (aux.prox != None):
            print(contador, aux.nome)
            contador += 1
            aux = aux.prox
        print(contador, aux.nome)

    def adicionar(self, novoElemento):
        
        if (self.cabeca == None):
            self.cabeca = novoElemento
            self.cauda = novoElemento
        else:
            self.cauda.prox = novoElemento
            self.cauda = novoElemento
            self.tamanho+=1#aumentando o tamnho da lista depois de add
        
    def remover(self):
        aux=self.cabeca
        self.cabeca=aux.prox # seria a mesma coisa de 
        #self.cabeca = self.cabeca.prox
        aux.prox = None
        self.tamanho-=1#aumentando o tamnho da lista depois de add

    def getTamanho(self):
        return self.tamanho 

filaDeAnimais = Fila()
peixe = Animal("Tilápia")
gato = Animal("Gato")
leao = Animal("Leão")
passaro = Animal("Pássaro")
macaco = Animal("Macaco")
tubarao = Animal("Tubarao")


filaDeAnimais.adicionar(macaco)
filaDeAnimais.adicionar(tubarao)

filaDeAnimais.imprimir()

print ("O tamanho é: ", filaDeAnimais.getTamanho())

print ("------------------")


