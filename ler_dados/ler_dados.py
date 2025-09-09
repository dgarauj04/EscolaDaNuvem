import csv

def ler_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            for linha in leitor_csv:
                print(linha)
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        
if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo CSV: ").strip()
    ler_dados(nome_arquivo)
    
# Para ler o arquivo csv dentro da pasta escrever_dados deve colocar:
# ler_dados/dados.csv        