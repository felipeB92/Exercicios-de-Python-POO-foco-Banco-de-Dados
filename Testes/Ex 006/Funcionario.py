from rich import print
from Pessoa import pessoa

class Funcionario(pessoa):
    def __init__(self, nome, idade,cargo,setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def Bater_Ponto(self):
        print(f'o funcionario [blue]{self.nome}[/] Bateu o ponto')