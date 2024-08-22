from pdf2docx import Converter
import os

# Define the file paths
pdf_file = 'My updated CV 2024.pdf'
docx_file = 'My updated CV 2024.docx'

# Check if the PDF file exists
if not os.path.exists(pdf_file):
    raise FileNotFoundError(f"The file {pdf_file} does not exist. Please check the file path.")

# Try to convert the PDF to DOCX
try:
    conv = Converter(pdf_file)
    conv.convert(docx_file, start=0, end=None)  # Convert the entire PDF
    conv.close()
    print(f"Conversion successful! The DOCX file has been saved as {docx_file}.")
except Exception as e:
    print(f"An error occurred during conversion: {e}")
