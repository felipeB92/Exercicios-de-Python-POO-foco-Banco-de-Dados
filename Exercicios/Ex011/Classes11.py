from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    def __init__(self,nome):
        self.nome = nome
        self.sal_Bruto = 0
        self.Sal_Min = 1672
        self.INSS = 7.5
        self.salario = 0

    @abstractmethod
    def Calc_Sallario(self):
        pass

    def Analisar_sal(self):
        print(Panel(f'O Salario de [blue]{self.nome}[/] ([red]funcionairo {self.Contrato}[/]) é de [green]R${self.salario:.2f}[/]  o correspondente a[yellow] {self.sal_Bruto/self.Sal_Min:.2f} salarios minimosn[/].', title="ANALISE SALARIAL",width=50))

class Horista(Funcionario):
    def __init__(self,nome,Valor_Hora,QTD_Horas):
        super().__init__(nome)
        self.val_hora = Valor_Hora
        self.qtd_hora = QTD_Horas
        self.Contrato = 'Horista'


    def Calc_Sallario(self):
       self.sal_Bruto = self.val_hora*self.qtd_hora
       self.salario = self.salario = self.sal_Bruto - ((self.sal_Bruto/100)*7.5)

class Mensalista(Funcionario):
    def __init__(self,nome,Salario_bruto):
        super().__init__(nome)
        self.sal_Bruto = Salario_bruto
        self.Contrato = 'Mensalista'

    def Calc_Sallario(self):
        self.salario = self.sal_Bruto - ((self.sal_Bruto / 100) * 7.5)


