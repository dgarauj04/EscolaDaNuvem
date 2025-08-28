# Função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento

def calcula_idade_em_dias(ano_nascimento):
    ano_atual = 2025
    idade_em_dias = (ano_atual - ano_nascimento) * 365
    return idade_em_dias

ano_de_nascimento = int(input("Digite o ano de nascimento: "))
idade_em_dias = calcula_idade_em_dias(ano_de_nascimento)
print(f"\nSua idade em dias é: {idade_em_dias} dias")