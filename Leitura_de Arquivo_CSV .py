import csv

def ler_arquivo_csv():
    # Solicitar o nome do arquivo CSV
    arquivo = input("Digite o nome do arquivo CSV a ser lido (ex: pessoas.csv): ")
    
    try:
        # Abrir o arquivo CSV para leitura
        with open(arquivo, mode='r', newline='') as file:
            reader = csv.reader(file)
            
            # Exibir cada linha como uma lista
            for linha in reader:
                print(linha)
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Chama a função para executar o código
ler_arquivo_csv()
