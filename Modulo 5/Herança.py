class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)
        
class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...

cliente1 = Cliente('Marcos', 'André')
cliente1.falar_nome_classe()
aluno1 = Aluno('Daibo', 'Pinto')
aluno1.falar_nome_classe()

