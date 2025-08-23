# cslculadora que realize as quatro operações basicas entre dois numeros / deve continuar pedindo ate que uma operacao seja concluida /dve ser capaz de lidar com diversos erros de entrada e operção / operações validas de adicao, subtracao, divisao e multiplicacao

while True:
    try:
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))
    except ValueError:
        print("Erro: Entrada inválida. Insira um número válido.")   
        continue
    
    operacao = input("Digite a operacao desejada (+, -, *, /): ")
           
    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        try:
            resultado = numero1 / numero2
        except ZeroDivisionError:
            print("Erro: Divisão por zero")
            continue
    else: 
        print("Erro: Operacao inválida. Use somente (+, -, *, /)")
        continue
    
    print(f"\n Resultado {numero1} {operacao} {numero2} = {resultado}")
    break