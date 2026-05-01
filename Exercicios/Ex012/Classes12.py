from abc import ABC, abstractmethod
from random import randint
from rich import print


class Personagen(ABC):
    def __init__(self,nome,vida):
        self.nome = nome
        self.vida = vida
        self.golpes= ['']



    def atacar(self,alvo,dano):
        self.dano = dano
        self.alvo = alvo
        print(f'o [blue]{self.tipo} {self.nome}[/] usou[purple] {self.golpes[randint(0,4)]}[/]')
        self.receberdano()

    def receberdano(self):
        self.dano_real = self.dano / (randint(1, 5))
        self.alvo.vida -= self.dano_real
        print(f'[blue]{self.alvo.nome}[/] recebeu [red]{self.dano_real:.0f}[/] de dano')
        if self.alvo.vida > 0:
            print(f'[blue]{self.alvo.nome}[/] ficou com {self.alvo.vida:.0f} de HP')
        else:
            print(f'[red]{self.alvo.nome} perdeu todo HP e morreu[/]')
        print()




    @abstractmethod
    def curar(self):
        pass

class mago(Personagen):
    def __init__(self,nome,vida):
        super().__init__(nome,vida)
        self.tipo = 'Mago'
        self.golpes = ['kamehameha','Magia de fogo','Relampago de plasma','Espada espiritual','Muralha de cistal']

    def curar(self):
        self.cura = 1 * (randint(1,100))
        if self.vida > 0:
            self.vida += self.cura
            print(f'O Mago {self.nome} usou uma magia de cura e recuperou [green]{self.cura}[/] de HP e ficou com {self.vida:.0f} de HP')
            print()
        else:
            pass

class guerreiro(Personagen):
    def __init__(self,nome,vida):
        super().__init__(nome,vida)
        self.tipo = 'Guerreiro'
        self.golpes = ['chute mortal','Helicoptero invertido','cabeçada','Pescotapa sonico','Soco na costela']

    def curar(self):
        if self.vida > 0:
            self.cura = 1 * (randint(1,100))
            print(f'O Guerreiro {self.nome} amarrou uma bandagem e recuperou [green]{self.cura}[/] de HP e ficou com {self.vida:.0f} de HP')
            print()
        else:
            pass
