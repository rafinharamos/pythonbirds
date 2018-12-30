class Pessoa:
    olhos = 2

    def __init__(self, *filhos,nome=None, idade=36):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola mundo {id(self)}'

if __name__ == "__main__":
    p = Pessoa()
    rafael = Pessoa('vicente','Roberto', nome='Rafael')
    cintia = Pessoa('vicente', 'roberto', nome='Cíntia', idade=39)
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Cintia'
    rafael.olhos = 1
    print(p.nome)
    for filhos in rafael.filhos:
     print(filhos)
    del rafael.filhos
    rafael.sobrenome = "Ramos"
    print(rafael.__dict__)
    print(cintia.__dict__)
    print(id(Pessoa.olhos), id(rafael.olhos), id(cintia.olhos))

