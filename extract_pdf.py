from pypdf import PdfReader

pdf_path = "data/raw/apollo_propulsion.pdf"

reader = PdfReader(pdf_path)

print("Number of pages:", len(reader.pages))

for page_number, page in enumerate(reader.pages, start=1):
    text = page.extract_text()

    print(f"\n{'=' * 60}")
    print(f"PAGE {page_number}")
    print(f"{'=' * 60}")

    print(text[:1000])