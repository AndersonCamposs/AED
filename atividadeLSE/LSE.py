from Animal import Animal
class LSE:

    def __init__ (self):
        #cabeca = atributo para representar o primeiro elemento
        self.cabeca=None
        #cauda = atributo para representar o último elemento
        self.cauda=None
        # atributo para definir o tamanho da lista
        self.tamanho=0
    
    def imprimir(self):
        if(self.cabeca==None):
            # 1ª questão
            print ("Lista vazia")
            return
        contador=0
        # aux = primeiro elemento, irá percorrer toda a lista
        aux = self.cabeca
        print(contador, aux.nome)
        # loop enquanto tiver um próximo elemento
        while (aux.prox != None):
            #aux será o próximo elemento
            aux=aux.prox
            contador+=1
            print(contador, aux.nome)

        
    
    # recebe como parametro um novo elemento
    def adicionarNoInicio(self, novo):
        novo.prox=self.cabeca #1o passo do quadro
        # verificar se é a primeira inserção, se for
        # o primeiro elemento (cabeca) também será o último
        # (cauda)
        if (self.cabeca==None):
            self.cauda = novo
            self.cabeca=novo #2o passo do quadro
            self.tamanho+=1#aumentando o tamnho da lista depois de add
   
    def adicionarEmQualquerIndice(self, novo,indice):
    # add no indice 0 é o mesmo que adicionar no início
        if (indice == 0 ):
            self.adicionarNoInicio(novo)
            # condição de qualquer indice diferente de zero
        
        elif (indice == self.tamanho):
            self.adicionarNoFim(novo)
        
        elif (self.cabeca == None):
            # 3ª questão
            print("A lista está vazia. O índice informado não existe.")
        
        elif (indice > self.tamanho):
            # 4ª questão
            print("O índice informado é maior que o tamanho da lista, portanto, ele não existe.")

        else:
            #criei uma variável aux para percorrer a lista
            aux=self.cabeca

            # variável para contar a posição
            posicao =0
            #enquanto a posicao for menor que o indice anterior
            #ao que quero adicionar, já que, precisamos apontar
            #o prox elemento do elemento anterior que irá add
            while (posicao< (indice-1)):
            #pulo
                aux=aux.prox
                posicao+=1

            novo.prox = aux.prox
            aux.prox=novo
            self.tamanho+=1#aumentando o tamnho da lista depois de add

    def adicionarNoFim(self,novo):
        if (self.cabeca == None):
            # 2ª questão
            self.adicionarNoInicio(novo)
        else:
            self.cauda.prox=novo
            self.cauda=novo
            self.tamanho+=1#aumentando o tamnho da lista depois de add

    def removerInicio(self):
        if (self.cabeca == None):
            # 5ª questão
            print("A lista já se encontra vazia.")
        else:
            aux=self.cabeca
            self.cabeca=aux.prox # seria a mesma coisa de
            #self.cabeca = self.cabeca.prox
            aux.prox = None
            self.tamanho-=1#aumentando o tamnho da lista depois de add
    
    def getTamanho(self):
        return self.tamanho
    
    def removerNoFim(self):
        if (self.cabeca == None):
            # 6ª questão
            print("A lista já se encontra vazia.")
        else:
            aux = self.cabeca
            anterior = None
            while aux.prox != None:
                anterior = aux
                aux = aux.prox
            anterior.prox = None
            self.cauda = anterior
            self.tamanho -= 1
    
    def removerEmQualquerIndice(self, indice):
        if (indice < 0):
            # 8ª questão
            print("A lista não possui índices negativos.")
            
        else:
        
            if (self.cabeca == None):
                # 7ª questão
                print("A lista já se encontra vazia.")
            
            elif (indice > self.tamanho - 1):
                print("O índice informado não existe.")

            else:
                if indice == 0:
                    self.removerInicio()
                    return
                
                elif (indice == self.tamanho - 1):
                    self.removerNoFim()
                    return
                
                else:
                    aux = self.cabeca
                    posicao = 0

                    while posicao < (indice - 1):
                        aux = aux.prox
                        posicao += 1
                    
                    remover = aux.prox
                    aux.prox = remover.prox
                    remover.prox = None
                    self.tamanho -= 1
