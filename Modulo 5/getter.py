class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta


c1= Caneta('azul')
print(c1.cor)

###############################################

#class Caneta:
#    def __init__(self, cor):
#        self.cor = cor

#    def get_cor(self):
#           return self.cor

#c1= Caneta('azul')
#print(c1.get_cor())
#print(c1.get_cor())
#print(c1.get_cor())
#print(c1.get_cor())

