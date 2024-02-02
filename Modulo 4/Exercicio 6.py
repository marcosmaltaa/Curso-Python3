import copy

def gerardeepcopy(dicionario, copiar):
    dicionario = copy.deepcopy(copiar)

    return dicionario


produtos=[
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.00},
    {'nome': 'Produto 3', 'preco': 15.50},
    {'nome': 'Produto 2', 'preco': 12.25},
    {'nome': 'Produto 4', 'preco': 69.00},
]

novos_produtos = []
produto_ordenado_nome=[]
produtos_ordenados_por_preco=[]

novos_produtos = gerardeepcopy(novos_produtos,produtos)
produto_ordenado_nome = gerardeepcopy(produto_ordenado_nome,produtos)
produtos_ordenados_por_preco = gerardeepcopy(produtos_ordenados_por_preco,produtos)

for produto in novos_produtos:
    produto['preco'] = produto['preco']*1.10

produto_ordenado_nome.sort(key=lambda x: x['nome'], reverse=True)
produtos_ordenados_por_preco.sort(key=lambda x: x['preco'])


print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produto_ordenado_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')
