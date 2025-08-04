import csv

def escrever_arquivo_csv():
    # Criar uma lista fictícia de pelo menos três pessoas
    dados_pessoas = [
        ['Nome', 'Idade', 'Cidade'],
        ['Guilherme', '16', 'Recife'],
        ['Gustavo', '16', 'Recife'],
        ['Natália', '40', 'Recife']
    ]
    
    # Solicitar o nome do arquivo CSV
    arquivo = input("Digite o nome do arquivo CSV (ex: pessoas.csv): ")
    
    try:
        # Abrir o arquivo CSV para escrita
        with open(arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Escrever os dados no arquivo CSV
            writer.writerows(dados_pessoas)
            
            # Exibe uma mensagem de confirmação
            print(f"Dados gravados com sucesso no arquivo '{arquivo}'.")
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Chama a função para executar o código
escrever_arquivo_csv()
