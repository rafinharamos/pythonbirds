from OO import motor, direcao

class Carro:
    def __init__(self,motor,direcao):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()


    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

if __name__=="__main__":
    carro = Carro(direcao, motor)
    carro.calcular_velocidade()
    carro.acelerar()
    carro.calcular_velocidade()
    carro.acelerar()
    carro.calcular_velocidade()
    carro.frear()
    carro.calcular_velocidade()
    carro.calcular_direcao()
    carro.girar_a_direita()
    carro.calcular_direcao()
    print(carro.direcao)
    carro.girar_a_esquerda()
    carro.calcular_direcao()
    print(carro.direcao)
    carro.girar_a_esquerda()
    carro.calcular_direcao()
    print(carro.direcao)



