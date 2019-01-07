DIRECOES = ['Norte', 'Leste', 'Sul', 'Oeste']


class Direcao:

    def __init__(self):
        self.__direcao = 0
        self.valor = DIRECOES[self.__direcao]

    def girar_a_direita(self):
        self.__direcao = (self.__direcao + 1) % len(DIRECOES)
        self.valor = DIRECOES[self.__direcao]

    def girar_a_esquerda(self):
        self.__direcao = (self.__direcao - 1) % len(DIRECOES)
        self.valor = DIRECOES[self.__direcao]


if __name__=="__main__":
    direcao = Direcao()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)

