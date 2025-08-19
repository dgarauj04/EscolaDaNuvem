# Programa que converte um valor em reais para dólares e euros

valor_reais = 100
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print(f"Para R$ {valor_reais} reais, você pode comprar US$ {valor_dolar:.2f} dólares ou € {valor_euro:.2f} euros.")
