nome= input("Digite seu nome: ")

num_carc=len(nome)

if num_carc <= 4:
    print("seu nome é curto")

elif num_carc >= 5 and num_carc <=6:
    print("seu nome é medio")

else:
    print("seu nome é grande")