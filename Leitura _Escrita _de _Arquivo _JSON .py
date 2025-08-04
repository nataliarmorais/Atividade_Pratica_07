import json

def ler_e_escrever_arquivo_json():
    # Criar um dicionário com dados de uma pessoa
    dados_pessoa = {
        'nome': 'Guilherme',
        'idade': 16,
        'cidade': 'Recife'
    }

    # Solicitar o nome do arquivo JSON
    arquivo = input("Digite o nome do arquivo JSON (ex: pessoa.json): ")

    try:
        # Escrever os dados no arquivo JSON
        with open(arquivo, mode='w', encoding='utf-8') as file:
            json.dump(dados_pessoa, file, indent=4)  # Salvar com formatação bonita (indentação)

        # Exibe mensagem de confirmação
        print(f"Dados gravados com sucesso no arquivo '{arquivo}'.")

        # Ler os dados do arquivo JSON
        with open(arquivo, mode='r', encoding='utf-8') as file:
            dados_lidos = json.load(file)
            print(f"\nDados lidos do arquivo '{arquivo}':")
            print(dados_lidos)

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
    
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{arquivo}' não é um arquivo JSON válido.")
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Chama a função para executar o código
ler_e_escrever_arquivo_json()
