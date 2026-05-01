from Classes12 import *

p1 = mago('Diego',3500)
p2 = guerreiro('Kratos',3500)


p1.atacar(p2,5000)
p2.curar()

p2.atacar(p1,5000)
p1.curar()