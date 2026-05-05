from abc import ABC, abstractmethod
from random import randint
from rich import print
from rich.panel import Panel
from rich.columns import Columns
from time import sleep

# TIPOS
#1 = Fogo
#2 = Agua
#3 = grama

class pokemon(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def Ataque(self,alvo):
        self.alvo = alvo
        print(f'{18*' '}[bold]INCIANDO BATALHA')
        self.painel()
        sleep(1)
        print()
        sleep(1)
        print(f'{self.nome} Atacou com {self.cor}{self.ataques[randint(0,3)]}')
        self.defesa()

    def defesa(self):
        self.dano = 10*(randint(5,6))
        if self.nivel > self.alvo.nivel:
            self.dano += (abs(self.nivel - self.alvo.nivel)/2)
        if self.nivel < self.alvo.nivel:
            self.dano -= (abs(self.alvo.nivel - self.nivel)/2)

        if self.tipo == 1 and self.alvo.tipo == 2 or self.tipo == 2 and self.alvo.tipo == 3 or self.tipo == 3 and self.alvo.tipo == 1:
            sleep(1)
            print(f'[orange1]não é ,muito efetivo[/]')
            self.dano -= abs(self.dano/randint(2,3))
        else:
            sleep(1)
            print(f'[bright_green]muito efetivo[/]')
            self.dano += abs(self.dano/randint(2,3))
        if self.dano <= 0:
            sleep(1)
            print(f'{self.nome} errou o ataque {self.alvo.nome} não recebeu dano')
        else:
            sleep(1)
            print(f'{self.alvo.nome} recebeu {self.dano:.0f} de dano')
            self.alvo.vida -= self.dano
        if self.alvo.vida <= 0:
            sleep(1)
            print(f'{self.alvo.nome} ficou sem HP e desmaiou')
            print(f'{self.cor}{self.nome} Venceu')
        else:
            sleep(1)
            print(f'{self.alvo.nome} Ficou com {self.alvo.vida:.0f} de HP')

    def painel(self):
        self.PAINEL = (Panel(f'LEVEL= {self.nivel}\nTIPO={self.tipoe}\nHP= {self.vida:.0f}\nATAQUES=\n{", ".join(self.ataques)}', title=f'{self.cor}{
            self.nome}',width=25))
        self.PAINEL2 = (Panel(f'LEVEL= {self.alvo.nivel}\nTIPO={self.alvo.tipoe}\nHP= {self.alvo.vida:.0f}\nATAQUES=\n{", ".join(self.alvo.ataques)}', title=f'{self.alvo.cor}{
            self.alvo.nome}',width=25))
        sleep(0.5)
        print(Columns([self.PAINEL,self.PAINEL2]))

class Charmander(pokemon):
    def __init__(self,nivel,nome='Charmander'):
        super().__init__(nome)
        self.nivel = nivel
        self.tipo = 1
        self.tipoe = 'Fogo'
        self.cor = '[red]'
        self.ataques = ['brasa','lança chamas','giro de fogo','investida de calor']

class Squirtle(pokemon):
    def __init__(self,nivel,nome='Squirtle'):
        super().__init__(nome)
        self.nivel = nivel
        self.tipo = 2
        self.tipoe = 'Agua'
        self.cor = '[blue]'
        self.ataques = ['jato de agua','bolhas','hidrobomba','cauda de gelo']

class Bulbasaur (pokemon):
    def __init__(self,nivel,nome='Bulbasaur'):
        super().__init__(nome)
        self.nivel = nivel
        self.cor = '[green]'
        self.tipo = 3
        self.tipoe = 'Grama'
        self.ataques = ['Chicote de cipo','pó venenosos','Folha de Navalha','Raio Solar']

def umatres(N):
    t= 0
    while True:
        try:
            t = int(input(f'{N}'))
            if t ==1 or t ==2 or t ==3:
                break
            else:
                print('opção invalida')
        except:
            print('invalido')
    return t

def eint(N):
    while True:
        try:
            t = int(input(f'{N}'))
            return t
        except:
            print('invalido')








