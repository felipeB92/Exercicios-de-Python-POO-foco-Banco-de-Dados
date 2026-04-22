from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    def __init__(self):
        pass

    def FerverAgua(self):
        print('1- Ferver Agua a 100°C ')

    def Preparar(self):
        print(f'=-=-=-Preparando Bebiba=-=-=-')
        self.FerverAgua()
        self.misturar()
        self.servir()
        print(f'=-=-=-Bebida Pronta =-=-=-')
        print()

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass



class Cafe(BebidaQuente):
    def __init__(self):
        print('-')

    def misturar(self):
        print('2- Passando Agua pressurizada pelo pó de cafe moido.')

    def servir(self):
        print('3- Servindo em Xicara pequena.')


class Cha(BebidaQuente):
    def __init__(self):
        print('-')

    def misturar(self):
        print('2- Mergulhando o sache e ervas na Agua.')

    def servir(self):
        print('3- Servindo em caneca de porcelana com limão.')

class Leite(BebidaQuente):
    def __init__(self):
        print('-')

    def misturar(self):
        print('2- Passando vapor pelo bico de leite.')

    def servir(self):
        print('3- Servindo em caneca Grande já com cafe.')


