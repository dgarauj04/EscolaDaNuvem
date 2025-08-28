# funcao que gera um perfil de usuario aleatorio usando random user generator, exibindo nome, email e pais

import requests

def gerar_perfil():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    dados = response.json()
    usuario = dados["results"][0]
    nome = usuario["name"]["first"] + " " + usuario["name"]["last"]
    email = usuario["email"]
    pais = usuario["location"]["country"]
    return nome, email, pais

nome, email, pais = gerar_perfil()
print("Perfil de usuário gerado:")
print(f"Nome: {nome}")
print(f"Email: {email}")
print(f"Pais: {pais}")