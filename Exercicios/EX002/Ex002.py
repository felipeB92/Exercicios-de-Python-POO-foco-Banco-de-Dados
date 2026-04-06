from rich import print
from rich.panel import Panel

class produto:
    def __init__(self,produto,preco):
        self.produto = produto
        self.preco = preco

    def etiqueta(self):
        sp ='R$'+str(self.preco)+"---"
        e = (36-len(self.produto))
        m = e//2*' '
        p = (36-len(sp))
        pm = p//2*'.'
        Eti = Panel(renderable= f'{m}{self.produto}\n{35*'-'}\n{pm}R${self.preco:.2f}{pm}',title='produto',title_align='center',subtitle_align='center',width=40)
        print(Eti)

c1 = produto('Borracha',0.50)
c1.etiqueta()

c2 = produto('Iphone',190000)
c2.etiqueta()
