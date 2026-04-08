from rich import print
from rich.panel import Panel

class ControleRemoto:
    canalmaximo = 5
    canalminimo = 1
    volumemaximo = 5
    volumeminimo = 1

    def __init__(self,canal = 1,volume = 1, Ligada = 'N'):
        self.canalatual = canal
        self.volumeatual = volume
        self.ligada = Ligada

    def Ligadesliga(self):
        if self.ligada == 'N':
            self.ligada = 'S'
        else:
            self.ligada = 'N'


    def mostrartv(self):
        if self.ligada == 'N':
            t = '   :electric_plug:[red]A TV ESTA DESLIGADA[/]'
        else:
            t = 'Canal  : '
            for c in range(self.canalminimo,self.canalmaximo+1):
                if c == self.canalatual:
                    t +=  f'[black on blue]{c}[/] '
                else:
                    t += f'{c} '
            t +='\nVolume : '
            for c in range(self.volumeminimo,self.volumemaximo+1):
                if c <= self.volumeatual:
                    t += f'[black on green] [/]'
                else:
                    t += f'[black on white] [/]'
        tv = Panel(renderable=t,title= 'TV',width=35)
        print(tv)
        print(f'< CH{self.canalatual} > - VOL{self.volumeatual} +\n')

    def canalmais(self):
        self.canalatual+= 1
        if self.canalatual > ControleRemoto.canalmaximo:
            self.canalatual = ControleRemoto.canalminimo
        return self.canalatual

    def canalmenos(self):
        self.canalatual -= 1
        if self.canalatual < ControleRemoto.canalminimo:
            self.canalatual = ControleRemoto.canalmaximo
        return self.canalatual

    def volumemais(self):
        self.volumeatual += 1
        if self.volumeatual > ControleRemoto.volumemaximo:
            self.volumeatual = self.volumemaximo
        return self.volumeatual

    def volumemenos(self):
        self.volumeatual -= 1
        if self.volumeatual < ControleRemoto.volumeminimo:
            self.volumeatual = self.volumeminimo
        return self.volumeatual


cont = str('')
c = 1
v = 1
L = 'S'
while True:
    print(10*'\n')
    TV = ControleRemoto(c, v, L)
    TV.mostrartv()
    cont = input(str(':'))
    if cont == '>':
        c = TV.canalmais()
    elif cont == '<':
        c = TV.canalmenos()
    elif cont == '+':
        v = TV.volumemais()
    elif cont == '-':
        v = TV.volumemenos()
    elif cont == '@':
        if L == 'N':
            L = 'S'
        else:
            L = 'N'
    elif cont == '0':
        break
    TV.mostrartv()
    cont = ''



