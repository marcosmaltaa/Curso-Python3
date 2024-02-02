def repeticao(lista):

    for sublista in lista:
        contagem = {}
        for elemento in sublista:
            if elemento in contagem:
                contagem[elemento] += 1
            else:
                contagem[elemento] = 1

        for elemento, quantidade in contagem.items():
            if quantidade > 1:
                print(f"{elemento} repete {quantidade} vezes")
        print()


l1 = [
    [1,2,3,4,5,2,1],
    [1,3,4,5,6,7,3],
    [7,9,6,5,8,7,6],
    [1,2,3,4,4,3,2],
    [1,1,1,1,3,3,4]
]

repeticao(l1)

