import fitz
import os
from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime

current_date = datetime.now()
if current_date.month == 1:
    previous_month = current_date.replace(year=current_date.year - 1, month=12)
else:
    previous_month = current_date.replace(month=current_date.month - 1)
month_year = current_date.strftime("%m%Y")

original_pdf_path = f'C:/Users/fahmi/OneDrive/Finances/Bank Statements/bank_statement_{month_year}.pdf'
trimmed_pdf_path = f'C:/Users/fahmi/OneDrive/Finances/Bank Statements/bank_statement_modified_{month_year}.pdf'
output_pdf_path = f'C:/Users/fahmi/OneDrive/Finances/Bank Statements/bank_statement_{month_year}_edited.pdf'

pdf_reader = PdfReader(original_pdf_path)
pdf_writer = PdfWriter()

# remove 2nd page
for page_num in range(len(pdf_reader.pages)):
    if page_num != 1:
        pdf_writer.add_page(pdf_reader.pages[page_num])

with open(trimmed_pdf_path, 'wb') as trimmed_pdf:
    pdf_writer.write(trimmed_pdf)
print(f"The new PDF without the second page has been saved as {trimmed_pdf_path}")

# redact unnecessary information
pdf_document = fitz.open(trimmed_pdf_path)
page = pdf_document.load_page(0)
page_width = page.rect.width
page_height = page.rect.height
section_height = page_height / 3
coordinates = [
    (0, section_height, page_width, 2 * section_height),
    (0, 2 * section_height, page_width, page_height)
]

for (x0, y0, x1, y1) in coordinates:
    page.draw_rect(fitz.Rect(x0, y0, x1, y1), color=(0, 0, 0), fill=(0, 0, 0))
print("Removed the unnecessary information from the PDF")

# redact lines that do not correspond to specified transactions
match_strings = ["GOCARDLESS", "35.00", "25.00"]

for page_num in range(1, len(pdf_document)):
    page = pdf_document.load_page(page_num)
    text_blocks = page.get_text("blocks")
    page_width = page.rect.width
    last_column_start_x = page_width * 4/5

    for block in text_blocks:
        text = block[4]
        if any(s in text for s in match_strings):
            x0, y0, x1, y1 = block[:4]
            page.draw_rect(fitz.Rect(last_column_start_x, y0, x1, y1), color=(0, 0, 0), fill=(0, 0, 0))
        else:
            x0, y0, x1, y1 = block[:4]
            page.draw_rect(fitz.Rect(x0, y0, x1, y1), color=(0, 0, 0), fill=(0, 0, 0))

pdf_document.save(output_pdf_path)
pdf_document.close()
os.remove(trimmed_pdf_path)
print(f"The modified PDF has been saved as {output_pdf_path}")
