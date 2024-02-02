"""Exercicio proposto onde averiguo se o valor digitado é par ou impar
    Caso o valor digitado seja diferente de inteiro vai rolar um erro"""
try:
    resposta = int(input("digite um numero: "))

    if(resposta % 2 == 0):
        print ("numero é par")

    else:
        print ("numero é impar")

except ValueError:
    print("o numero precisa ser inteiro")


