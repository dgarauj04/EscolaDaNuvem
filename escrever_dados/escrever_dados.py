import csv

def escrever_dados(nome_arquivo , dados):
    try:
        with open(nome_arquivo, 'w') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow(["Nome", "Idade", "Cidade"])
            for dado in dados:
                escritor_csv.writerow(dado)
        print(f"Dados escritos no arquivo {nome_arquivo} com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever os dados no arquivo: {e}")        

        
dados = [
    ["Douglas", 20, "Itaborai"],
    ["Mikaela", 32, "Sao Paulo"],
    ["Bartolomeu", 37, "Belo Horizonte"],
    ["Sara", 22, "Rio de Janeiro"]
]

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo CSV: ").strip()
    escrever_dados(nome_arquivo, dados)
    
# Para escrever o arquivo csv dentro da pasta escrever_dados deve colocar:
# escrever_dados/dados.csv    