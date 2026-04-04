from rich import print
from rich.table import Table

tabela = Table(title='exemplo de tabela')
tabela.add_column('produto',justify="center",style="bold")
tabela.add_column('Preço',justify="center", style="cyan")
tabela.add_row('TV','[bold red]R$1000,50[/]')
tabela.add_row('pendrive','R$25,99')

print(tabela)