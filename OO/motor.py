class Motor:
    def __init__(self,velocidade=0):
        self.velocidade = velocidade


    def acelerar(self):
        self.velocidade += 1
        return self.velocidade

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0
        return self.velocidade

if __name__=="__main__":
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.acelerar()
    motor.acelerar()
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)




