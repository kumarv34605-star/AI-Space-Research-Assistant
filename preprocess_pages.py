import json
from preprocessing import clean_text


INPUT_PATH = "data/filtered_ocr_pages.json"
OUTPUT_PATH = "data/cleaned_ocr_pages.json"


with open(INPUT_PATH, "r", encoding="utf-8") as f:
    pages = json.load(f)


cleaned_pages = []

for page in pages:
    cleaned_pages.append(
        {
            "page": page["page"],
            "source": page["source"],
            "text": clean_text(page["text"])
        }
    )


with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(
        cleaned_pages,
        f,
        indent=2,
        ensure_ascii=False
    )


print(f"Processed {len(cleaned_pages)} pages.")
print(f"Saved to {OUTPUT_PATH}")