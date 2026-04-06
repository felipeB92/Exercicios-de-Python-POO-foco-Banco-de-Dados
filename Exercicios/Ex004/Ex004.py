from rich import print
from time import sleep


class livro:
    def __init__(self,Titulo,paginas,lidas=1):
        self.Titulo = Titulo
        self.paginas = paginas
        self.lidas = lidas
        print(f'voce abriu o livro [blue]{self.Titulo}[/] que tem [blue]{paginas}[/] paginas \nAgora voce esta na pagina {self.lidas} ')

    def avançar_paginas(self,paginas=0):
        P = paginas
        V = 0
        for c in range (1 , P+1):
            if self.lidas >= self.paginas:
                break
            self.lidas += 1
            V += 1
            sleep(0.5)
            print(f'=>{self.lidas}',end=' ')
        print(f'Você avançou {V} e agora esta na pagina {self.lidas}')
        if self.lidas == self.paginas:
            print(f'[red]Voce chegou ao final do livro{self.Titulo}[/]')
            print(40*'=-')
        V = 0


l1 = livro('Arte da guerra',20)
l1.avançar_paginas(5)
l1.avançar_paginas(10)
l1.avançar_paginas(100)

l2 = livro('Como falar com Gatos',15)
l2.avançar_paginas(5)
l2.avançar_paginas(7)
l2.avançar_paginas(20)