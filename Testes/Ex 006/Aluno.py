from rich import print
from Pessoa import pessoa

class Aluno(pessoa):
    def __init__(self,nome,idade,curso,turma):
        super().__init__(nome , idade)
        self.curso = curso
        self.turma = turma

    def Fazer_Matricula(self):
        print(f'O aluno [blue]{self.nome}[/] Fez a matricula')