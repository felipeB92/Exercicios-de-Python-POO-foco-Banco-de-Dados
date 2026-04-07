from pygments.styles.dracula import yellow
from rich import print

class caneta:
    def __init__(self,cor):
        self.ca = cor
        if cor.lower() == 'vermelho':
            c = 'red'
        elif cor.lower() == 'verde':
            c = 'green'
        elif cor.lower() == 'azul':
            c = 'blue'
        elif cor.lower() == 'amarelo':
            c = 'yellow'
        else:
            c = 'bold'
        self.cor = c
        self.tampa = 's'

    def destampar(self):
        self.tampa = 'n'

    def quebralinha(self,Quantidade):
            for c in range(0,Quantidade):
                if c == 0:
                    print(f'\n')
                else:
                    print(f' ')

    def escreva(self,texto):
        if self.tampa == 'n':
            print(f'[{self.cor}]{texto}[/]',end= ' ')
        else:
            print(f'A caneta {self.ca} esta tampada')

# cores de caneta disponivel
# azul, vermelho, verde, amarelo


c1 = caneta('Vermelho')
c2 = caneta('Azul')
c3 = caneta('Verde')
c4 = caneta('Amarelo')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escreva('Ola tudo bem!')
c1.quebralinha(2)
c2.escreva('Como vai voce?')
c3.escreva('Vai a aula Hoje?')
c3.quebralinha(1)
c4.escreva('Hoje não vou estou com preguiça')
