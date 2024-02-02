import os
lista = []

while True:
    print("Selecione o que deseja fazer: ")
    escolha = input("[I]nserir [D]eletar [V]isualizar: ")

    if escolha == "i":
        os.system('cls')
        objeto = input("Digite o item que deseja: ")
        lista.append(objeto)

    elif escolha == "d":
        os.system('cls')
        if not lista:
            print('Lista esta vazia!!!')
        else:
            objeto = int(input("Qual indicie que deseja retirar: "))
            del lista[objeto]

    elif escolha == "v":
        os.system('cls')
        for numero, nome in enumerate(lista):
            print(numero, nome)
    
    else:
        print("Valor não reconhecido, tente novamente")
        

