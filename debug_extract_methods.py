from pypdf import PdfReader


pdf_path = "data/raw/apollo_propulsion.pdf"

reader = PdfReader(pdf_path)

# PDF page 6 → Python index 5
page = reader.pages[5]


print("=" * 70)
print("METHOD 1: DEFAULT EXTRACTION")
print("=" * 70)

text_default = page.extract_text()

print(text_default)


print("\n" + "=" * 70)
print("METHOD 2: LAYOUT EXTRACTION")
print("=" * 70)

text_layout = page.extract_text(
    extraction_mode="layout"
)

print(text_layout)