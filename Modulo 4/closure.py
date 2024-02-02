def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def executa(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

soma_5 = executa(soma, 5)

print(soma_5(6))




    