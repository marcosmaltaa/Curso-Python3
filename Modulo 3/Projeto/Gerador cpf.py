import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

cpf = nove_digitos
cpf_primeiro = cpf[:9]
cpf_lista = [int(digito) for digito in cpf_primeiro]
num1= 10
result=[]

for i in range(1,10,1):
    result.append(cpf_lista[i-1] * num1)
    num1 = num1 - 1

soma = sum(result) * 10

if soma%11 > 9:
    cpf_primeiro_digito = 0
else:
    cpf_primeiro_digito = soma%11

num1= 11
result.clear()
cpf_segundo = cpf_primeiro + str(cpf_primeiro_digito)
cpf_lista2 = [int(digito) for digito in cpf_segundo]

for i in range(1,11,1):
    result.append(cpf_lista2[i-1] * num1)
    num1 = num1 - 1

soma = sum(result)*10
if soma%11 > 9:
    cpf_segundo_digito = 0
else:
    cpf_segundo_digito = soma%11

cpf_gerado = cpf_primeiro + str(cpf_primeiro_digito) + str(cpf_segundo_digito)

print(cpf_gerado)