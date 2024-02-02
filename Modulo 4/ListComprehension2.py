nomes = ['Marcos', 'Felipe', 'Luiz', 'Maria', 'Ana']
novos_nomes=[f'{nome[:-1].lower()}{nome[-1].upper()}' for nome in nomes]


print(novos_nomes)