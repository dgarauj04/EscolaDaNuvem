# Programa que calcula o desconto em uma loja.

produto = "Camiseta"
preco = 50.00
desconto = 20

valor_desconto = preco * (desconto / 100)

novo_preco = preco - valor_desconto

print(f"O produto '{produto}' com valor R$ {preco:.2f} vai custar R$ {novo_preco:.2f} com {desconto}% de desconto.")