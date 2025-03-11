import pdfplumber
import pandas as pd

def read_pdf_to_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def save_text_to_excel(text, excel_path):
    # Split the text into lines
    lines = text.split('\n')
    # Create a DataFrame
    df = pd.DataFrame(lines, columns=["Text"])
    # Save the DataFrame to an Excel file
    df.to_excel(excel_path, index=False)

def main():
    pdf_path = r'C:\Users\00082300\Desktop\E115 EP3-RB-03\DF-1153-34 Ângulo de colagem BF (TIP) - TE glue cap (TIP) Rev0.pdf'  # Replace with the path to your PDF file
    excel_path = r'C:\Users\00082300\Desktop\E115 EP3-RB-03\DF-1153-34 Ângulo de colagem BF (TIP) - TE glue cap (TIP) Rev0.xlsx'  # Replace with the path to your output Excel file
    
    # Read PDF and extract text
    pdf_text = read_pdf_to_text(pdf_path)
    
    # Save the extracted text to an Excel file
    save_text_to_excel(pdf_text, excel_path)
    
    print(f'Text from {pdf_path} has been saved to {excel_path}')

if __name__ == "__main__":
    main()
