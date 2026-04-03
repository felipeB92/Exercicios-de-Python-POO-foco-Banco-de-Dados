class NOME:
    def __init__(self,):
        self.nome = ''
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} tem {self.idade} anos'

p1 = NOME()
p1.nome = 'diego'
p1.idade = 6
p1.aniversario()
print(p1.mensagem())

p2 = NOME()
p2.nome = 'Isabella'
p2.idade = 12
print(p2.mensagem())
