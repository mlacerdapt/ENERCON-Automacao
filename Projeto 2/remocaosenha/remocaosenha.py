from openpyxl import load_workbook

def remove_sheet_protection(file_path):
    # Carregar a planilha
    workbook = load_workbook(filename=file_path)
    
    # Percorrer todas as planilhas e remover a proteção
    for sheet in workbook.worksheets:
        if sheet.protection.sheet:
            sheet.protection.sheet = False
            print(f"Proteção removida da planilha: {sheet.title}")

    # Salvar o arquivo com um novo nome
    new_file_path = file_path.replace(".xlsx", "_unprotected.xlsx")
    workbook.save(new_file_path)
    print(f"Arquivo salvo como: {new_file_path}")

if __name__ == "__main__":
    file_path = "remocaosenha/Orçamento (tambor de accionamento)_Luísa.xlsx"  # Substitua pelo caminho do seu arquivo protegido
    remove_sheet_protection(file_path)
