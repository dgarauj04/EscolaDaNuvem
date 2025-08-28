# Funcao que consulta a cotacao atual de uma moeda estrangeira em relacao ao real, usuario deve informar o codigo da moeda desejada e o o programa deve exibir máximo e mínimo da cotação, além da data e hora da última atualização, utilizar AwesomeAPi

import requests
import json
import datetime

def consultar_cotacao_moeda(codigo_moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL"
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()
    cotacao = dados[codigo_moeda.upper() + "BRL"]["bid"]
    cotacao_max = dados[codigo_moeda.upper() + "BRL"]["high"]
    cotacao_min = dados[codigo_moeda.upper() + "BRL"]["low"]
    data_hora = dados[codigo_moeda.upper() + "BRL"]["create_date"]
    data_hora = datetime.datetime.strptime(data_hora, "%Y-%m-%d %H:%M:%S")
    return cotacao, cotacao_max, cotacao_min, data_hora

moeda = input("Digite o código da moeda desejada(ex: USD, EUR, BTC): ").upper()

cotacao, cotacao_max, cotacao_min, data_hora = consultar_cotacao_moeda(moeda)
print(f"Cotação de {moeda}/BRL")
print(f"Valor da cotação: {cotacao}")
print(f"Máximo: {cotacao_max}")
print(f"Mínimo : {cotacao_min}")
print(f"Data e hora da última atualização: {data_hora}")