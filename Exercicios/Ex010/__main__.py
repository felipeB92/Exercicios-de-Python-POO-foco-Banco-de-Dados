from rich.table import Table

from Classes import *
from rich import print
from rich import table

dist = 55

Viagen = [moto(dist),caminhao(dist),drone(dist)]

tabela = Table(title='TABELA DE FRETES')
tabela.add_column('Distancia')
tabela.add_column('Tipo')
tabela.add_column('Frete')

for c in Viagen:
    tabela.add_row(f'{dist}Km',f'{type(c).__name__}',f'{c.cal_frete()}')

print(tabela)

