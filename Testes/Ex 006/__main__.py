from rich import print
from rich import inspect
from Aluno import Aluno
from Professor import Professor
from Funcionario import Funcionario

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