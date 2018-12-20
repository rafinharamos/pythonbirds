class Pessoa:
    def __init__(self, *filhos,nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola mundo {id(self)}'

if __name__ == "__main__":
    p = Pessoa()
    Rafael = Pessoa('vicente','Roberto', nome='Rafael')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Cintia'
    print(p.nome)
    for filhos in Rafael.filhos:
     print(filhos)
    del Rafael.filhos
    print(Rafael.__dict__)

