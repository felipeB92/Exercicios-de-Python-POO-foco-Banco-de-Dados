from abc import ABC, abstractmethod
from random import randint

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
        print(f'{self.nome} Atacou com {self.cor}{self.ataques[randint(0,3)]}\033[m')
        self.defesa()

    def defesa(self):
        self.dano = 100/(randint(1,5))
        if self.nivel >= self.alvo.nivel:
            self.dano += (abs(self.alvo.nivel - self.nivel))/2
        else:
            self.dano -= (abs(self.alvo.nivel - self.nivel))/2

        if self.tipo == 1 and self.alvo.tipo == 2 or self.tipo == 2 and self.alvo.tipo == 3 or self.tipo == 3 and self.alvo.tipo == 1:
            print('\033[36;1mnão é ,muito efetivo\033[m')
            self.dano -= (self.dano/100)*(randint(10,20))
        else:
            print('\033[33;1mmuito efetivo\033[m')
            self.dano += (self.dano / 100) * (randint(10, 20))
        if self.dano <= 0:
            print(f'{self.nome} errou o ataque {self.alvo.nome} não recebeu dano')
        else:
            print(f'{self.alvo.nome} recebeu {self.dano:.0f} de dano')
            self.alvo.vida -= self.dano
        if self.alvo.vida <= 0:
            print(f'{self.alvo.nome} ficou sem HP e desmaiou')
        else:
            print(f'{self.alvo.nome} Ficou com {self.alvo.vida:.0f} de HP')


class Charmander(pokemon):
    def __init__(self,nivel,nome='Charmander'):
        super().__init__(nome)
        self.nivel = nivel
        self.tipo = 1
        self.cor = '\033[31;1m'
        self.ataques = ['brasa','lança chamas','giro de fogo','investida de calor']

class Squirtle(pokemon):
    def __init__(self,nivel,nome='Squirtle'):
        super().__init__(nome)
        self.nivel = nivel
        self.tipo = 2
        self.cor = '\033[34;1m'
        self.ataques = ['jato de agua','bolhas','hidrobomba','cauda de gelo']

class Bulbasaur (pokemon):
    def __init__(self,nivel,nome='Bulbasaur'):
        super().__init__(nome)
        self.nivel = nivel
        self.cor = '\033[32;1m'
        self.tipo = 3
        self.ataques = ['Chicote de cipo','pó venenosos','Folha de Navalha','Raio Solar']






