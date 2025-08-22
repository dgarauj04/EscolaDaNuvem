# calcular o indice de massa corporal de uma pessoa
print("O IMC é calculado da seguinte forma: \nIMC = peso / altura²\n")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print(f"Seu imc é: {imc:.2f} \n")

if imc < 18.5:
    print("Classificação:Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obeso")    