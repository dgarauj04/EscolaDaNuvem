# ler nome, salario, total de vendas feitas pelo vendedor e informar o total a receber ao mes com 15% de comissao

nome = input("Digite o nome do vendedor: ")
salario = float(input("Digite o salario fixo do vendedor: "))
total_de_vendas = float(input("Digite o total de vendas feitas pelo vendedor no mês: "))

comissao = total_de_vendas * (15 / 100)
total_receber = salario + comissao

print(f"\nO vendedor {nome} deverá receber R$ {total_receber:.2f} no mês com uma comissão de R$ {comissao:.2f}")