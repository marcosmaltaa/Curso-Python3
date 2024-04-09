class Caneta:
    def __init__(self, cor):
        self._cor= cor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor


c1= Caneta('azul')
c1.cor = 'Rosa'
print(c1.cor)