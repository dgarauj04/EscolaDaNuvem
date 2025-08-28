# função que gera uma senha aleatoria com random, com caracteres especiais

import random
import string

def gerar_senha(tamanho):
    caracteres = (string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + "!@#$%&*^()-=+,._:;<>[]{}/?")
    
    return ''.join(random.choice(caracteres) for i in range(tamanho))
    

tamanho_senha = int(input("Digite o tamanho da senha: "))
senha = gerar_senha(tamanho_senha)
print(f"Senha gerada: {senha}")