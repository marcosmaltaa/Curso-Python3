def par_impar(x):
    if(x%2 == 0):
        return "par"
    else:
        return "impar"

num1 = int(input("Digite um numero: "))

resultado = par_impar(num1)
print(resultado)