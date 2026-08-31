import json


with open("data/cleaned_ocr_pages.json", "r", encoding="utf-8") as f:
    pages = json.load(f)


for page in pages:

    if page["page"] == 6:

        print("=" * 70)
        print("CLEANED PAGE 6")
        print("=" * 70)

        print(page["text"])