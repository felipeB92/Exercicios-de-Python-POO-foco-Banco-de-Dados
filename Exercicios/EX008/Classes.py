from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self,lados):
        self.qtd_lados = lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class circulo(Poligono):
    def __init__(self,lados):
        super().__init__(lados)
        self.raio = lados
        self.pi = 3.14159


    def area(self):
        self.area = ((self.raio*self.raio)*self.pi)
        print (f'Area = {self.area:.1f}')

    def perimetro(self):
        self.perimetro = ((self.raio * 2)*self.pi)
        print (f'perimetro = {self.perimetro:.1f}')

class quadrado(Poligono):
    def __init__(self,lados):
        super().__init__(lados)
        self.lado = lados

    def area(self):
        self.area = self.lado*(self.lado)
        return print (f'Area = {self.area:.1f}')

    def perimetro(self):
        self.perimetro = (self.lado*4)
        return print (f'Perimetro = {self.perimetro:.1f}')



