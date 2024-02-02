def criarMultiplicador(multiplcador):
    def multiplicar(numero):
        return numero * multiplcador
    return multiplicar

duplicar = criarMultiplicador(2)

print(duplicar(2))