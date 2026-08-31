import pdfplumber


pdf_path = "data/raw/apollo_propulsion.pdf"


with pdfplumber.open(pdf_path) as pdf:

    page = pdf.pages[5]  # PDF page 6

    text = page.extract_text()

    print("=" * 70)
    print("PDFPLUMBER EXTRACTION")
    print("=" * 70)

    print(text)