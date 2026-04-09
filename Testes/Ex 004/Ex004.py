from rich import print
from rich import inspect

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(pessoa):
    def __init__(self,nome,idade,curso,turma):
        super().__init__(nome , idade)
        self.curso = curso
        self.turma = turma

    def Fazer_Matricula(self):
        print(f'O aluno [blue]{self.nome}[/] Fez a matricula')

class Professor(pessoa):
    def __init__(self, nome, idade,especialidade,nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def Dar_Aula(self):
        print(f'o professor [blue]{self.nome}[/] deu uma Aula')

class Funcionario(pessoa):
    def __init__(self, nome, idade,cargo,setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def Bater_Ponto(self):
        print(f'o funcionario [blue]{self.nome}[/] Bateu o ponto')

a1 = Aluno('Diego',6,'Informatica','T027')
a1.fazer_aniversario()
a1.Fazer_Matricula()
inspect(a1, methods=True)

p1 = Professor('Lucia',85,'matematica','aposentada')
p1.Dar_Aula()
p1.fazer_aniversario()
inspect(p1, methods=True)

f1 = Funcionario('Pedro',37,'Lider','Operação')
f1.Bater_Ponto()
inspect(f1, methods=True)