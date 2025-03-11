import os
import pandas as pd
import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
import re
from reportlab.lib.units import inch
from tkinter import messagebox
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))
 
# ------------------------------
# Constants
# ------------------------------
file_suffixes = {
    "Blank E175 Trimmed": "1076809",
    "Web LE1": "1072866",
    "Pre-Final": "1076797",
    "Blank Assembled": "",
    "Blade bonding and demolding": "1077199",
    "TE-UD SF": "1072100",
    "RB Suction Shell": "1071970",
    "TE-UD PF": "1072101",
    "Spar Boom PF": "1071389",
    "Spar Boom SF": "1070521",
    "Web TE1": "1072519",
    "Web TE2": "1072520",
    "Leading Edge Cover": "1071929",
    "Leading Edge CAP - Flange": "1076217",
    "Leading Edge CAP - Tip": "1076218",
    "Trailing Edge CAP - Tip": "1076215",
    "Web LE3": "1076242",
    "Web LE2": "1072867",
    "Trailing Edge CAP - Flange": "1076214",
    "Preform Seg1": "1070660",
    "PS1 LE-TE": "1070661",
    "PS3 LE-TE": "1070659",
    "RB Pressure Shell": "1071969",
    "Web Flatback": "1100017",
    "Final Finish": " ",
}
 
# New dictionary with file name information (Portuguese translation)
nome_ficheiros = {
    "Blank E175 Trimmed": "Pá Rebarbada E175",
    "Web LE1": "Alma BA1",
    "Pre-Final": "Pré Finish",
    "Blank Assembled": "Pá Confeccionada",
    "Blade bonding and demolding": "Pá Fechada",
    "TE-UD SF": "TE-UD LS",
    "RB Suction Shell": "Casca Lado Pressão",
    "TE-UD PF": "TE-UD LP",
    "Spar Boom PF": "Longarina Lado Pressão",
    "Spar Boom SF": "Lognarina Lado Sucção",
    "Web TE1": "Alma BF1",
    "Web TE2": "Alma BF2",
    "Leading Edge Cover": "Cobertura do Bordo de Ataque",
    "Leading Edge CAP - Flange": "Bordo de Ataque - Flange",
    "Leading Edge CAP - Tip": "Bordo de Ataque - Tip",
    "Trailing Edge CAP - Tip": "Bordo de Fuga - Tip",
    "Web LE3": "Alma BA3",
    "Web LE2": "Alma BA2",
    "Trailing Edge CAP - Flange": "Bordo de Fuga - Flange",
    "Preform Seg1": "Peforma Segmento 1",
    "PS1 LE-TE": "PS1 BA-BF",
    "PS3 LE-TE": "PS3 BA-BF",
    "RB Pressure Shell": "Casca Lado Pressão",
    "Web Flatback": "Alma Flatback",
    "Final Finish": "Final Finish",
}
 
# ------------------------------
# Utility Functions
# ------------------------------
def extract_numeric(serial):
    match = re.search(r'\d+', serial)
    return int(match.group()) if match else None
 
def get_translation(prefix):
    # Return the translation from the nome_ficheiros dictionary (or "N/A" if not found)
    return nome_ficheiros.get(prefix, "N/A")
 
def draw_header(canvas, prefix, prefixpt, serial_number, doc):
    # Path to the logo (adjust if necessary)
    logo_path = r"O:\02-Blades\19-QA-Engineers\18.Dados da Inspecao E175\Bases Auxiliarres\enerconlogo.png"
 
    # Set the position and dimensions for the logo
    logo_width = 1 * inch      # 1 inch wide
    logo_height = 0.5 * inch   # 0.5 inch tall
    logo_x = 20                # X position from the left margin
    logo_y = 755               # Y position
 
    # Draw the logo
    try:
        canvas.drawImage(logo_path, logo_x, logo_y, width=logo_width, height=logo_height, mask='auto')
    except Exception as e:
        st.error(f"Error loading logo: {e}")
 
    # Calculate the starting position for header text (to the right of the logo)
    text_x = logo_x + logo_width + 10
    text_y = logo_y + (logo_height / 2)
   
    # Draw the header text in one line: "SerialNumber Prefix / Translation"
    canvas.setFont("Arial-Bold", 12)
    header_text = f"E175 {serial_number} {prefix} / {prefixpt}"
    canvas.drawString(text_x, text_y, header_text)
 
def add_footer(canvas, doc):
    page_number = doc.page
    canvas.setFont("Arial", 10)
    canvas.drawString(500, 20, f"Page {page_number}")
 
def generate_pdf(df, prefix, serial_number, output_dir):
    if df.empty:
        st.error("No data to generate PDF.")
        return
 
    # Rename "EN" column to "Description"
    if "EN" in df.columns:
        df = df.rename(columns={"EN": "Description"})
    # Rename "PT" column to "Descrição" if it exists
    if "PT" in df.columns:
        df = df.rename(columns={"PT": "Descrição"})
 
    # Remove unwanted columns
    columns_to_remove = ["Process", "Characteristic Code", "Serial Number"]
    df = df.drop(columns=[col for col in columns_to_remove if col in df.columns])
 
    # Use ReportLab's Paragraph objects for automatic text wrapping.
    styles = getSampleStyleSheet()
    # Define a fixed font size
    fixed_font_size = 8
    # Set the normal style to use Helvetica with the desired font size
    normal_style = styles["Normal"]
    normal_style.fontName = "Arial"
    normal_style.fontSize = fixed_font_size
 
    if "Description" in df.columns:
        df["Description"] = df["Description"].astype(str).apply(lambda x: Paragraph(x, normal_style))
    if "Descrição" in df.columns:
        df["Descrição"] = df["Descrição"].astype(str).apply(lambda x: Paragraph(x, normal_style))
 
    # Prepare table data: header row plus data rows.
    table_data = [list(df.columns)] + df.values.tolist()
 
    suffix = file_suffixes.get(prefix, "default")
    pdf_file = os.path.join(output_dir, f"{prefix}-{suffix}_{serial_number}.pdf")
    doc = SimpleDocTemplate(pdf_file, pagesize=letter, rightMargin=20, leftMargin=20, topMargin=30, bottomMargin=30)
 
    elements = []
 
    # Define fixed column widths.
   
    col_widths = []
    for col in df.columns:
        if col == "Description":
            col_widths.append(150)
        elif col == "Descrição":
            col_widths.append(150)
        elif col in ["Code",]:
            col_widths.append(40)
        elif col in ["Valuation"]:
            col_widths.append(50)
        elif col == "Inspection Data":
            col_widths.append(130)
        else:
            col_widths.append(50)
 
    table = Table(table_data, colWidths=col_widths, repeatRows=1)
 
    style_table = TableStyle([
    ('FONTSIZE', (0, 0), (-1, -1), fixed_font_size),
    ('FONTNAME', (0, 0), (-1, 0), 'Arial-Bold'),  # Header row in Arial-Bold
    ('FONTNAME', (0, 1), (-1, -1), 'Arial'),      # Body rows in Arial
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
])
 
    # Apply conditional formatting for the "Valuation" column if present.
    if "Valuation" in df.columns:
        valuation_index = df.columns.get_loc("Valuation")
        for i, row in enumerate(df.itertuples(index=False), start=1):
            value = getattr(row, "Valuation", "")
            if value == "Reproved":
                style_table.add('BACKGROUND', (valuation_index, i), (valuation_index, i), colors.red)
            elif value == "Approved":
                style_table.add('BACKGROUND', (valuation_index, i), (valuation_index, i), colors.green)
 
    table.setStyle(style_table)
    elements.append(table)
 
    try:
        doc.build(
            elements,
            onFirstPage=lambda canvas, doc: draw_header(canvas, prefix, get_translation(prefix), serial_number, doc),
            onLaterPages=lambda canvas, doc: (
                draw_header(canvas, prefix, get_translation(prefix), serial_number, doc),
                add_footer(canvas, doc)
            )
        )
        st.success(f"PDF generated: {pdf_file}")
        return pdf_file
    except Exception as e:
        st.error(f"Error generating PDF: {e}")
 
# ------------------------------
# Streamlit App
# ------------------------------
st.title("Excel to PDF Converter")
 
uploaded_files = st.file_uploader("Upload Excel Files", type="xlsx", accept_multiple_files=True)
serial_numbers_input = st.text_input("Enter Serial Numbers (comma-separated)")
start_serial = st.text_input("Start Serial Number")
end_serial = st.text_input("End Serial Number")
# Change the default output directory to your desired path.
output_dir = st.text_input("Output Directory", value=r"O:\02-Blades\19-QA-Engineers\18.Dados da Inspecao E175\Protocolos")
 
if st.button("Generate PDFs"):
    if not uploaded_files:
        st.error("Please upload at least one Excel file.")
    elif not serial_numbers_input and not (start_serial and end_serial):
        st.error("Please enter serial numbers or a valid range.")
    else:
        for uploaded_file in uploaded_files:
            try:
                df = pd.read_excel(uploaded_file)
                prefix = os.path.splitext(uploaded_file.name)[0]
 
                if 'Serial Number' not in df.columns:
                    st.error(f"'Serial Number' column not found in {uploaded_file.name}")
                    continue
 
                unique_serial_numbers = df['Serial Number'].unique()
                valid_serials = set()
 
                # Use the comma-separated serial numbers provided by the user.
                if serial_numbers_input:
                    serial_numbers = [sn.strip() for sn in serial_numbers_input.split(',')]
                    for serial in serial_numbers:
                        if serial in unique_serial_numbers:
                            valid_serials.add(serial)
 
                # Alternatively, if a range is provided, use that.
                if start_serial and end_serial:
                    start_serial_num = extract_numeric(start_serial)
                    end_serial_num = extract_numeric(end_serial)
                    for serial in unique_serial_numbers:
                        serial_num = extract_numeric(serial)
                        if serial_num and start_serial_num <= serial_num <= end_serial_num:
                            valid_serials.add(serial)
 
                if not valid_serials:
                    st.warning(f"No valid serial numbers found in {uploaded_file.name}.")
                    continue
 
                # Generate a PDF for each valid serial number.
                for serial_number in valid_serials:
                    filtered_data = df[df['Serial Number'] == serial_number]
                    pdf_path = generate_pdf(filtered_data, prefix, serial_number, output_dir)
                    st.write(f"Download [PDF]({pdf_path})")
            except Exception as e:
                st.error(f"Error processing {uploaded_file.name}: {e}")
 