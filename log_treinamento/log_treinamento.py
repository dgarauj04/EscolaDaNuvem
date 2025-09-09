import pandas as pd

def calcular_tempo(nome_arquivo):
    try: 
        df = pd.read_csv(nome_arquivo)
        tempo_media = df['tempo_execucao'].mean()
        tempo_desvio = df['tempo_execucao'].std()
        print(f"Média do tempo de execução: {tempo_media:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {tempo_desvio:.2f} segundos")
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")   

nome_arquivo = calcular_tempo(input("Digite o nome do arquivo: "))
    
# Para pegar o arquivo csv dentro da pasta log_treinamento deve colocar:
# log_treinamento/dados_log.csv