from rich import print

class funcionario:
    def __init__(self,nome,setor,cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentação(self):
        return f':handshake: Ola sou [blue]{self.nome}[/] {self.cargo} do setor {self.setor} na empresa MMDNET!'

c1 = funcionario('Jurema','limpeza','lider')
print(c1.apresentação())

c2 = funcionario('Diego','Administrativo','Analista')
print(c2.apresentação())