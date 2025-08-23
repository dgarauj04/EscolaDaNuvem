# Solicitar numeros inteiros e continuar ate o usuario digitar fim / deve informar se e par ou impar / se nao for inteiro deve informar e continuar / no final exibir a quantidade de pares e impares

pares = 0
impares = 0

while True:
    numero_inteiro = input("Digite um numero inteiro ou 'fim' para sair: ")
    
    if numero_inteiro.lower() == 'fim':
        break
    try:
        numero = int(numero_inteiro)
        if numero % 2 == 0:
            print(f"O numero {numero} é par")
            pares += 1
        else:
            print(f"O numero {numero} é impar")
            impares += 1
    except ValueError:
        print(f"Erro: '{numero_inteiro}' não é um número inteiro valido.")
        continue

print(f"\nQuantidade de numeros pares: {pares}")
print(f"Quantidade de numeros impares: {impares}")