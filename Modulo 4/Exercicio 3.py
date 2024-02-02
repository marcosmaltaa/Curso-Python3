perguntas= [{
    'pergunta': 'Quanto é 2+2?',
    'opcoes': ['1','3','5','4'],
    'resposta': '4',
},

{
    'pergunta': 'Quanto é 2 X 5?',
    'opcoes': ['10','19', '20', '25'],
    'resposta': '10',
},

{
    'pergunta': 'Quanto é 25/5?',
    'opcoes':['10', '5', '2', '3'],
    'resposta': '5',
}
]

for i in range(len(perguntas)):
    print(perguntas [i]['pergunta'])
    
    for j in range(len(perguntas[i]['opcoes'])):
        print(perguntas[i]['opcoes'][j])
    
    resultado = input("Resposta: ")
    if resultado == perguntas[i]['resposta']:
        print('Acertou!')
    else:
        print('Errou!')

    print()

    
