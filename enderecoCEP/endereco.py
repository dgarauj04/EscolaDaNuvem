# Funcao que consulte informacao de endereco a partir do cep fornecido, utilizando ViaCEP, deve exibir logradouro, bairro, cidade e estado

import requests

def consultar_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()
    logradouro = dados['logradouro']
    bairro = dados['bairro']
    cidade = dados['localidade']
    estado = dados['uf']
    
    return logradouro, bairro, cidade, estado

endereco = input("Digite o CEP: ")
logradouro, bairro, cidade, estado = consultar_endereco(endereco)
print("\nInformações do Endereço:")
print(f"Logradouro: {logradouro}")
print(f"Bairro: {bairro}")
print(f"Cidade: {cidade}")
print(f"Estado: {estado}")
