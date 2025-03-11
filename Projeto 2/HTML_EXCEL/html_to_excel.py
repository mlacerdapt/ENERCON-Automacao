import pandas as pd

# Função para converter HTML em Excel
def convert_html_to_excel(html_file, excel_file):
    # Ler o arquivo HTML
    tables = pd.read_html(html_file)

    # Verifica se há tabelas no HTML
    if not tables:
        print("Nenhuma tabela encontrada no arquivo HTML!")
        return

    # Se houver mais de uma tabela, você pode escolher qual tabela usar
    # Aqui, vamos apenas usar a primeira tabela
    df = tables[0]

    # Converter para Excel
    df.to_excel(excel_file, index=False)

    print(f"Arquivo Excel criado com sucesso: {excel_file}")

# Caminho do arquivo HTML e do arquivo Excel de saída
html_file_path = r'C:\Users\00082300\Downloads\Projeto 2\HTML_EXCEL\Export SAP\Gerente de atividades - SAP Manufacturing Execution - SAP SE.html'  # Substitua pelo caminho do seu arquivo HTML
excel_file_path = r'C:\Users\00082300\Downloads\Projeto 2\HTML_EXCEL\Export SAP\Gerente de atividades - SAP Manufacturing Execution - SAP SE.xlsx'  # Substitua pelo caminho do arquivo Excel de saída

# Chamar a função de conversão
convert_html_to_excel(html_file_path, excel_file_path)
