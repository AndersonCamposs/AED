class Produto:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.prox = None
        self.ant = None