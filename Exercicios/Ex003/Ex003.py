from rich import print
from rich.panel import Panel

class Churras:
    def __init__(self,titulo,quantidade):
        self.titulo = titulo
        self.quantidade = quantidade

    def analisar(self):
        totalcarne = 0.400*self.quantidade
        totalvalor = totalcarne * 82.40
        valorporpessoa = totalvalor / self.quantidade
        tabela = Panel(title=self.titulo,renderable=f'''Analisando [blue]{self.titulo}[/] com [yellow]{self.quantidade}[/] de amigos\nCada participante comera 0.4Kg e cada Kg custa R$82,40 \nRecomendo comprar [blue]{totalcarne}Kg [/]de carne\nO custo total sera de[green]R${totalvalor:.2f}[/]\nCada pessoa devera Pagar[yellow] R${valorporpessoa}[/] para participar.''')
        print(tabela)

c1 = Churras('Churras na praia',15)
c1.analisar()
