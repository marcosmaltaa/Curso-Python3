def multiplica(*args):
    tamanho= 1
    for numero in args:
        tamanho = tamanho*numero
        
    return tamanho



digito= 1,2,3,4,5
resultado = multiplica(*digito)
print(resultado)