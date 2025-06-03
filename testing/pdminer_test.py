from pdfminer.high_level import extract_text
pdf_path = "resume.pdf"
text = extract_text(pdf_path)
print(text)