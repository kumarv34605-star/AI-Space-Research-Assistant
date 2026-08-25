from pypdf import PdfReader
import json

pdf_path = "data/raw/apollo_propulsion.pdf"

reader = PdfReader(pdf_path)

pages = []

for page_number, page in enumerate(reader.pages, start=1):

    text = page.extract_text() or ""

    pages.append({
        "page": page_number,
        "text": text.strip()
    })

with open("data/extracted_pages.json", "w", encoding="utf-8") as f:
    json.dump(pages, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(pages)} pages.")
print("Saved to data/extracted_pages.json")