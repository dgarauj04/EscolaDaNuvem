# Função que deve calcular gorjeta com base no valor total da conta e na porcentagem desejada da gorjeta

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

total_conta = float(input("Digite o valor total da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

gorjeta = calcular_gorjeta(total_conta, porcentagem)

print(f"\nPara a conta de R$ {total_conta}, com uma gorjeta de {porcentagem:.2f}%, o valor da gorjeta é: R$ {gorjeta}")