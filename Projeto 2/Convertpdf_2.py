import pdfplumber
import pandas as pd

def extract_tables_from_pdf(pdf_path):
    tables = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                print(f"Processing page {i+1} of {len(pdf.pages)}")
                try:
                    table = page.extract_table()
                    if table:
                        df = pd.DataFrame(table[1:], columns=table[0])
                        tables.append(df)
                        print(f"Table found on page {i+1}")
                    else:
                        print(f"No table found on page {i+1}")
                except Exception as e:
                    print(f"Error extracting table on page {i+1}: {e}")
    except Exception as e:
        print(f"Error opening PDF: {e}")
    return tables

def save_tables_to_excel(tables, output_path):
    try:
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            for i, table in enumerate(tables):
                table.to_excel(writer, sheet_name=f"Table_{i+1}", index=False)
        print(f"Tables successfully saved to {output_path}")
    except Exception as e:
        print(f"Error saving tables to Excel: {e}")

def process_pdf_file(pdf_path, output_path):
    tables = extract_tables_from_pdf(pdf_path)
    if tables:
        save_tables_to_excel(tables, output_path)
    else:
        print("No tables were found in the PDF.")

# Paths to the input PDF and output Excel file
pdf_path = r'C:\Users\00082300\Downloads\Projeto 2\Desenhos\D02904945_2.1_Rev2.1 RBL Schale DS Innenlaminat – PS RB shell inner laminate (E-175 EP5-RB-01).pdf'
output_path = r'C:\Users\00082300\Downloads\Projeto 2\Desenhos\D02904945_2.1_Rev2.1 RBL Schale DS Innenlaminat – PS RB shell inner laminate (E-175 EP5-RB-01).xlsx'

# Process the PDF and save the tables to an Excel file
process_pdf_file(pdf_path, output_path)
