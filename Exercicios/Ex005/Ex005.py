from rich import print
from rich.panel import Panel


class gamer:
    def __init__(self,Nome,Nick):
        self.nome = Nome
        self.nick = Nick
        self.lista = []

    def add_Favorito(self,Favorito):
        self.lista.append(Favorito)

    def ficha(self):
        listao = sorted(self.lista)
        t = ''
        for c in range (0,len(listao)):
            if c == len(listao)-1:
                t += ':video_game:[bold blue] '+ listao[c]
            else:
                t += ':video_game:[bold blue] ' + listao[c] + '\n'

        ficha = Panel(title=f'Jogador <{self.nick}>',renderable=f'Nome real: [bold black on blue]{self.nome}[/]\nJogos favoritos:\n{t}')
        print(ficha)



j1 = gamer('Diego','diegozila')
j1.add_Favorito('Minecraft')
j1.add_Favorito('Roblox')
j1.add_Favorito('Mario Maker')
j1.ficha()


j2 = gamer('Felipe','F3L1P3')
j2.add_Favorito('Zelda')
j2.add_Favorito('God of War')
j2.add_Favorito('Kof')
j2.add_Favorito('Sheep Rider')
j2.add_Favorito('Megaman 2')
j2.ficha()

j3 = gamer('Alice','AliceMons')
j3.add_Favorito('Mercado')
j3.add_Favorito('Minecraft')
j3.ficha()
