import json
import pdfplumber
import pytesseract


# Tesseract installation
pytesseract.pytesseract.tesseract_cmd = (
    r"D:\Tools\Tesseract-OCR\tesseract.exe"
)

PDF_PATH = "data/raw/apollo_propulsion.pdf"
OUTPUT_PATH = "data/ocr_pages.json"


def extract_pages_with_ocr(pdf_path):
    pages = []

    with pdfplumber.open(pdf_path) as pdf:

        for page_number, page in enumerate(pdf.pages, start=1):

            print(f"OCR processing page {page_number}/{len(pdf.pages)}...")

            # Convert PDF page into an image
            image = page.to_image(resolution=300).original

            # Extract text from the image using Tesseract
            text = pytesseract.image_to_string(image)

            pages.append({
                "page": page_number,
                "source": "apollo_propulsion.pdf",
                "text": text.strip()
            })

    return pages


pages = extract_pages_with_ocr(PDF_PATH)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(pages, f, ensure_ascii=False, indent=2)

print()
print(f"Processed {len(pages)} pages.")
print(f"Saved to {OUTPUT_PATH}")