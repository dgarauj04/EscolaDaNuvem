# Calculadora de número Inteiro

A = int(input("Digite o primeiro número inteiro: "))
B = int(input("Digite o segundo número inteiro: "))
C = int(input("Digite o terceiro número inteiro: "))
D = int(input("Digite o quarto número inteiro: "))

diferenca = (A * B - C * D)
print("Fórmula para calcular a diferença: (A * B - C * D)")
print(f"Fórmula com os valores fornecidos ({A} * {B} - {C} * {D})")
print(f"O resultado da DIFERENCA = {diferenca}")
# ou pode ser feito da seguinte forma:
print(f"O resultado da DIFERENCA = {A * B - C * D}")
