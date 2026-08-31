import pdfplumber


pdf_path = "data/raw/apollo_propulsion.pdf"

pages_to_check = [6, 7, 10, 20, 30, 40]


with pdfplumber.open(pdf_path) as pdf:

    for page_number in pages_to_check:

        page = pdf.pages[page_number - 1]

        text = page.extract_text()

        print("\n" + "=" * 70)
        print(f"PAGE {page_number}")
        print("=" * 70)

        print(text[:1000])