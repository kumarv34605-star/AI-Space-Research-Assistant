from pypdf import PdfReader


pdf_path = "data/raw/apollo_propulsion.pdf"

reader = PdfReader(pdf_path)

page = reader.pages[5]   # Python index 5 = PDF page 6

text = page.extract_text()

print(text)