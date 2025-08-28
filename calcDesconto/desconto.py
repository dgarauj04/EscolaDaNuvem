# Programa que receba preco e percentual de desconto e calcule o preco final

def calcular_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return preco_final

preco = float(input("Digite o preço do produto: "))
percentual = float(input("Digite o percentual de desconto: "))
        
preco_com_desconto = calcular_desconto(preco, percentual)
print(f"\nPreço final de R${preco} do produto com {percentual:.2f}% de desconto é: R$ {preco_com_desconto:.2f}")
    
