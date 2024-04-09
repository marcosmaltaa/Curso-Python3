import json
CAMINHO_ARQUIVO = 'exercicio_1.json'

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
p1 = Pessoa('Marcos', 'Andre', 21)
p2 = Pessoa('Rodrigo', 'Vieira', 33)
p3 = Pessoa('Leonardo', 'Reis', 11)
bd =[vars(p1),vars(p2),vars(p3)]

with open (CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii= False, indent= 2)