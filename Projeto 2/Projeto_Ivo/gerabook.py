import os
import PyPDF4
import pandas as pd
 
# Define the directory where the PDF files are located
directory = r'O:\02-Blades\19-QA-Engineers\25.Dados da Inspeção E175\Protocolos'
 
# Define the path to the Excel file that contains the PDF file names
excel_file = r'O:\02-Blades\19-QA-Engineers\18.Dados da Inspecao E175\Bases Auxiliarres\ListaDeComponentes.xlsx'
 
# Define the name of the column in the Excel file that contains the final merged PDF file name
output_column = 'Denominacao'
 
# Open the Excel file and read the data
df = pd.read_excel(excel_file)
 
# Loop through each row in the Excel file
for index, row in df.iterrows():
    # Create a PdfFileMerger object to merge the PDF files
    merger = PyPDF4.PdfFileMerger()
 
    # Loop through each column in the current row, including the output_column
    for column in row.index:
        # Get the PDF name for the current column and row
        pdf_name = str(column) + '_' + str(row[column]) + '.pdf'
 
        # Define the full path for the PDF file
        pdf_path = os.path.join(directory, pdf_name)
 
        # Clean up the file path by removing any extra whitespace
        filename, extension = os.path.splitext(pdf_path)
        filename = filename.strip()
        pdf_path = filename + extension
 
        # Attempt to read and append the PDF file if it exists
        try:
            with open(pdf_path, 'rb') as pdf_file:
                merger.append(PyPDF4.PdfFileReader(pdf_file))
        except (FileNotFoundError, PyPDF4.utils.PdfReadError) as e:
            print(f'Error reading PDF file: {pdf_path}\nError: {e}')
            continue
 
        # Print the path of each added file for debugging purposes
        print(f"Added: {pdf_path}")
 
    # Get the final name for the merged PDF file from the `Finish-` column
    output_name = str(row[output_column])
 
    # Define the full path for the final merged PDF file
    output_path = os.path.join(directory, output_name + '.pdf')
 
    # Save the merged PDF file
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)
 
    print(f"Merged PDF saved as: {output_path}")
 