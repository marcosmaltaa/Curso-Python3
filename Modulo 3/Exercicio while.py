nome = input("Digite seu nome:  ")
car_nome = len(nome)
i= 0
novo_nome = ""
print (f"seu nome é: %s" % (nome))
print (f"tem %d de tamanho" % (car_nome))

while i < car_nome:
    novo_nome += f'{nome[i]}*'
    i += 1


print(f"*{novo_nome}")

