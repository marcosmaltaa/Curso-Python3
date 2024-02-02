while True:
    num1= input("Digite um numero: ")
    num2= input("Digite outro numero: ")
    operador = input("Escolha o operador +, -, *, /:  ")
    numero_valido = None
    operadores_validos = '+-/* '

    try:
        num1_float= float(num1)
        num2_float= float(num2)
        numero_valido = True
    except:
        numero_valido = None

    if numero_valido is None:
        print("O numero digitado é invalido")
        continue
    
    if operador not in operadores_validos:
        print("Operador invalido")
        continue

    if operador == "+":
        print(num1_float + num2_float)
    elif operador == "-":
        print(num1_float - num2_float)
    elif operador == "*":
        print(num1_float * num2_float)
    else:
        print(num1_float / num2_float)
    

    sair = input("Digite [s]air para sair").lower().startswith('s')
    if(sair==True):
        break
    