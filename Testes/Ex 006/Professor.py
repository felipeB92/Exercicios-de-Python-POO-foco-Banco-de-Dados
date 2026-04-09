from rich import print
from Pessoa import pessoa

class Professor(pessoa):
    def __init__(self, nome, idade,especialidade,nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def Dar_Aula(self):
        print(f'o professor [blue]{self.nome}[/] deu uma Aula')