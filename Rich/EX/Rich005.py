from rich import print
from rich.traceback import install
install()

def divisao(x , y):
    return x/y
#ira retornar erro de divisão por zero
print(divisao(2,0))