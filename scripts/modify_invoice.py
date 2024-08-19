import pdfplumber
import os
from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime

current_date = datetime.now()
month_year = current_date.strftime("%m%Y")

# path to your PDF file
original_pdf_path = f'C:/Users/fahmi/OneDrive/Finances/Bank Statements/bank_statement_{month_year}.pdf'
trimmed_pdf_path = f'C:/Users/fahmi/OneDrive/Finances/Bank Statements/bank_statement_modified_{month_year}.pdf'

pdf_reader = PdfReader(original_pdf_path)
pdf_writer = PdfWriter()

for page_num in range(len(pdf_reader.pages)):
    if page_num != 1:
        pdf_writer.add_page(pdf_reader.pages[page_num])

with open(trimmed_pdf_path, 'wb') as trimmed_pdf:
    pdf_writer.write(trimmed_pdf)

print(f"The new PDF without the second page has been saved as {trimmed_pdf_path}")

# with pdfplumber.open(pdf_path) as pdf:
#     # Extract text from each page
#     for page in pdf.pages:
#         text = page.extract_text()
#         print(text)  # Print or process the text
