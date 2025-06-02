from pdfminer.high_level import extract_text

# Path to the PDF file
pdf_path = "resume.pdf"

# Extract text
text = extract_text(pdf_path)

# Print the extracted text
print(text)