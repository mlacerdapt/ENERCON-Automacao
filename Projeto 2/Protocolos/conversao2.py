import os
import fitz  # PyMuPDF
from docx import Document

def pdf_para_word(pasta_origem, pasta_destino):
    # Verifica se a pasta de destino existe, senão, cria
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Lista todos os arquivos na pasta de origem
    arquivos = os.listdir(pasta_origem)
    
    # Filtra apenas arquivos PDF
    arquivos_pdf = [arq for arq in arquivos if arq.lower().endswith('.pdf')]
    
    for arquivo_pdf in arquivos_pdf:
        caminho_pdf = os.path.join(pasta_origem, arquivo_pdf)
        caminho_docx = os.path.join(pasta_destino, arquivo_pdf.replace('.pdf', '.docx'))
        
        # Cria um novo documento Word
        doc = Document()
        
        # Abre o PDF
        pdf_document = fitz.open(caminho_pdf)
        
        # Itera pelas páginas do PDF
        for num_pagina in range(len(pdf_document)):
            pagina = pdf_document[num_pagina]
            texto = pagina.get_text("text")
            
            # Adiciona o texto ao documento Word
            doc.add_paragraph(texto)
        
        # Salva o documento Word
        doc.save(caminho_docx)
        
        print(f"Convertido: {arquivo_pdf} para {arquivo_pdf.replace('.pdf', '.docx')}")

# Exemplo de uso
pasta_origem = r'C:\Users\00082300\Downloads\Projeto 2\Protocolos\Protocolos'  
pasta_destino = r'C:\Users\00082300\Downloads\Projeto 2\Protocolos\Protocolos'  

pdf_para_word(pasta_origem, pasta_destino)
