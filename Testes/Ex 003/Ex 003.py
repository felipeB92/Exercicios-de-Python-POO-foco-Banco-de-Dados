class ContaBancaria:
    """
    cria conta BAncaria e permite realizar saques e depositos
    """
    def __init__(self,id,nome,saldo=0):
        self.id = id
        self.titular = nome
        self.Saldo = saldo
        print(f'Conta criada com sucesso Saldo inicial de R${self.Saldo:.2f} reais')

    def __str__(self):
        return f'A conta {self.id} do titular {self.titular} tem saldo R${self.Saldo:.2f} '

    def depositar(self,valor):
        self.Saldo += valor
        print(f'\033[1;32m Deposito de R${valor:.2f} realizado com sucesso\033[m')

    def saque(self,valor):
        if self.Saldo > valor:
            self.Saldo -= valor
            print(f'\033[1;32m Saque de R${valor:.2f} realizado com sucesso\033[m')
        else:
            saldo = self.Saldo
            print('\033[1;31mSaldo insuficiente\033[m')


c1 = ContaBancaria(123,'Diego',1500)
c1.depositar(500)
c1.saque(1350)
print(c1)

