from pygments.lexers import j

from Batalha import *
from rich import print

print(f'[1][green]bulbasaur')
print(f'[2][blue]squirtle')
print(f'[3][red]charmander')

J= umatres('Escolha seu pokemon: ')
n= eint('Qual nivel do seu pokemon: ')

i= randint(1,3)
while J == i:
    i = randint(1,3)

n2 =randint(10,100)
if J == 3:
    p1 = Charmander(n)
if J == 2:
    p1 = Squirtle(n)
if J == 1:
    p1 = Bulbasaur(n)

if i == 3:
    p2 = Charmander(n2)
if i == 2:
    p2 = Squirtle(n2)
if i == 1:
    p2 = Bulbasaur(n2)

while True:
    if p1.vida <= 0:
        break
    else:
        p1.Ataque(p2)
    if p2.vida <=0:
        break
    else:
        p2.Ataque(p1)

print('fim da batalha')


