from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self,Distancia):
        self.Distancia = Distancia

    def Distancia(self):
        pass

    def frete(self):
        pass

    @abstractmethod
    def cal_frete(self):
        pass

class moto(Transporte):
    def __init__(self,Distancia):
        super().__init__(Distancia)
        self.fator = 0.50


    def cal_frete(self):
        R = self.Distancia * self.fator
        return f'{R:.2f}'

class caminhao(Transporte):
    def __init__(self,Distancia):
        super().__init__(Distancia)
        self.fator = 1.20
        self.fretemin = 50


    def cal_frete(self):
        if self.Distancia < self.fretemin:
            return 'DISTANCIA MINIMA DE FRETE 50Km'
        else:
            R = self.Distancia * self.fator
            return f'{R:.2f}'

class drone(Transporte):
    def __init__(self,Distancia):
        super().__init__(Distancia)
        self.fator = 9.50
        self.fretemax = 10

    def cal_frete(self):
        if self.Distancia > self.fretemax:
            return 'DISTANCIA MAXIMA DE FRETE 10Km'
        else:
            R = self.Distancia * self.fator
            return f'{R:.2f}'