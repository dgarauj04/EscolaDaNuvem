import json 

def escrever_dados(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w') as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
        print(f"Dados escritos no arquivo {nome_arquivo} com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever no arquivo: {e}")
        
dados = {
    "nome": "Mikaela",
    "idade": 22,
    "cidade": "Rio de Janeiro"
}        
         
def ler_dados(nome_arquivo):
    try:        
        with open(nome_arquivo, 'r') as arquivo_json:
            dados_lidos = json.load(arquivo_json)
        print(f"\nDados lidos do arquivo: {dados_lidos}")
        
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} nao foi encontrado.")
        
if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo JSON: ")
    escrever_dados(nome_arquivo, dados)
    ler_dados(nome_arquivo)
    
# Para ler e escrever o arquivo json dentro da pasta escrever_ler_dados deve colocar:
# escrever_ler_dados/dados.json