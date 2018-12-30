class Pessoa:
    def __init__(self, *filhos,nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola mundo {id(self)}'

if __name__ == "__main__":
    p = Pessoa()
    rafael = Pessoa('vicente','Roberto', nome='Rafael')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Cintia'
    print(p.nome)
    for filhos in rafael.filhos:
     print(filhos)
    del rafael.filhos
    rafael.sobrenome = "Ramos"
    print(rafael.__dict__)

