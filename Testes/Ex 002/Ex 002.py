class NOME:
    def __init__(self,nome='Vazio',idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos'

p1 = NOME('Diego',6)
p1.aniversario()
print(p1)

p2 = NOME('Isabella',12)
print(p2)
