import json
import pdfplumber

PDF_PATH = "data/raw/nasa_systems_engineering_handbook.pdf"
OUTPUT_PATH = "data/handbook_pages.json"


pages = []

with pdfplumber.open(PDF_PATH) as pdf:

    print(f"Total pages: {len(pdf.pages)}")

    for page_number, page in enumerate(pdf.pages, start=1):

        text = page.extract_text()

        if text:
            text = text.strip()
        else:
            text = ""

        pages.append({
            "page": page_number,
            "source": "nasa_systems_engineering_handbook.pdf",
            "text": text
        })

        print(f"Processed page {page_number}/{len(pdf.pages)}")


with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(pages, f, indent=2, ensure_ascii=False)


print("\nExtraction complete.")
print(f"Saved to: {OUTPUT_PATH}")