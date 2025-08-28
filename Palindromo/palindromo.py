# Criar função que verifica se uma palavra é um palíndromo

def palindromo(texto):
    texto_limpo = ''.join(palavra.lower() for char in texto if char.isalnum())
    return texto_limpo == texto_limpo[::-1]

palavra = input("Digite uma palavra: ")
resultado = palindromo(palavra)

if resultado == True:
        resposta = "Sim"
else:
        resposta = "Não"

print(f"A palavra {palavra} é um palindromo? {resposta}")