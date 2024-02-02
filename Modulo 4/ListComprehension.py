def divisaoFn(x, y):
    return x/y

def multiplicaFn(x, y):
    return x*y

def potenciaFn(x,y):
    return x**y

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
divide = [divisaoFn(numero,2) for numero in numeros]
multiplica = [multiplicaFn(numero,2) for numero in numeros]
potencializa = [potenciaFn(numero,2) for numero in numeros]
impares = [numero for numero in numeros if numero % 2 != 0]
pares = [numero for numero in numeros if numero % 2 == 0]

print(numeros)
print(divide)
print(multiplica)
print(potencializa)
print(impares)
print(pares)
