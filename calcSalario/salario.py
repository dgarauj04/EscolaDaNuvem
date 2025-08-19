"""
Ler o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. Calcular o salário do funcionário e exibir o resultado formatado corretamente
"""

numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor que recebe por hora: "))

salario = horas_trabalhadas * valor_hora

print(f"\nO salário do funcionário {numero_funcionario} é de R$ {salario:.2f} reais")