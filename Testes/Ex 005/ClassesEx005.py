from rich import print

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