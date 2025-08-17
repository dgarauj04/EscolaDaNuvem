# Calculadora de número Inteiro

A = int(input("Digite o primeiro número inteiro: "))
B = int(input("Digite o segundo número inteiro: "))
C = int(input("Digite o terceiro número inteiro: "))
D = int(input("Digite o quarto número inteiro: "))

diferenca = (A * B - C * D)
print(f"DADOS = {A}, {B}, {C} e {D}")
print(f"DIFERENCA = {diferenca}")
# ou pode ser feito da seguinte forma:
print(f"DIFERENCA = {A * B - C * D}")
