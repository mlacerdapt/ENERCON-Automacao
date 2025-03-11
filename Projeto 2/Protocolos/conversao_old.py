import os
import pdfplumber
import pandas as pd

def buscar_pdf(pasta):
    # Procura por arquivos PDF na pasta especificada
    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.pdf'):
            return os.path.join(pasta, arquivo)
    return None

def converter_pdf_para_excel(caminho_pdf, caminho_excel):
    dados = []

    # Abre o PDF e extrai o texto
    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if texto:
                linhas = texto.split('\n')
                for linha in linhas:
                    # Divide a linha em colunas sempre que encontrar '/'
                    colunas = linha.split('/')
                    dados.append(colunas)

    # Converte a lista de dados em um DataFrame
    df = pd.DataFrame(dados)

    # Salva o DataFrame como um arquivo Excel
    df.to_excel(caminho_excel, index=False, header=False)

def main():
    pasta = r'C:\Users\00082300\Downloads\Projeto 2\Protocolos'  # Substitua pelo caminho da pasta onde o PDF está
    caminho_pdf = buscar_pdf(pasta)

    if caminho_pdf:
        caminho_excel = caminho_pdf.replace('.pdf', '.xlsx')
        converter_pdf_para_excel(caminho_pdf, caminho_excel)
        print(f'Conversão concluída. Arquivo Excel salvo em: {caminho_excel}')
    else:
        print('Nenhum arquivo PDF encontrado na pasta especificada.')

if __name__ == '__main__':
    main()
