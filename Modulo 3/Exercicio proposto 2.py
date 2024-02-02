horario = int(input("Digite um horario: "))

if (horario>= 0 and horario<=11):
    print("Bom dia")

elif (horario>=12 and horario<=17):
    print("Boa Tarde")

elif (horario>=18 and horario<=23):
    print("Boa noite")

else:
    print("horario invalido")