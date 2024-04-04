from Animal import Animal

class Pilha:
    
    def __init__(self) -> None:
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    def imprimir(self):
        aux = self.cabeca
        if (self.cabeca == None):
            print("Lista vazia.")
            return
        
        contador = self.tamanho - 1
        while (aux.prox != None):
            print(contador, aux.nome)
            contador -= 1
            aux = aux.prox
        print(contador, aux.nome)

   
    def empilhar(self, novoElemento):
        novoElemento.prox = self.cabeca
        if (self.cabeca == None):
            self.cauda = novoElemento
        self.cabeca = novoElemento
        self.tamanho+=1#aumentando o tamnho da lista depois de add
        
    def desempilhar(self):
        aux=self.cabeca
        self.cabeca=aux.prox # seria a mesma coisa de 
        #self.cabeca = self.cabeca.prox
        aux.prox = None
        self.tamanho-=1#aumentando o tamnho da lista depois de add

    

    def getTamanho(self):
        return self.tamanho 



pilhaDeAnimais = Pilha()
peixe = Animal("Tilápia")
gato = Animal("Gato")
leao = Animal("Leão")
passaro = Animal("Pássaro")
macaco = Animal("Macaco")
tubarao = Animal("Tubarao")


pilhaDeAnimais.empilhar(macaco)
pilhaDeAnimais.empilhar(tubarao)

pilhaDeAnimais.imprimir()

print ("O tamanho é: ", pilhaDeAnimais.getTamanho())

print ("------------------")
pilhaDeAnimais.desempilhar()
pilhaDeAnimais.imprimir()
print ("O tamanho é: ", pilhaDeAnimais.getTamanho())
