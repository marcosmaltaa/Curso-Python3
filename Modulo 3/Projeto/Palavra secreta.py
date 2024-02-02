import random
palavras = ['problema', 'dinheiro', 'palavra', 'sorte', 'pagamento', 'investimento', 'acao']
palavra = random.choice(palavras)
tamanho= len(palavra)
secreta = "*" * tamanho

while True:
    tentativa = input("Digite uma letra: ")

    if tentativa in palavra:
        for i in range(tamanho):
            if tentativa == palavra[i]:
                secreta = secreta[:i] + tentativa + secreta[i+1:]
        print(secreta)

        if secreta == palavra:
            print("Parabéns! Você adivinhou a palavra!")
            break
    else:
        print("Letra incorreta. Tente novamente.")