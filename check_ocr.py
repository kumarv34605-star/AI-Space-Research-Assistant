import json


with open("data/ocr_pages.json", "r", encoding="utf-8") as f:
    pages = json.load(f)


for page in pages:

    if page["page"] in [6, 30]:

        print("=" * 70)
        print(f"PAGE {page['page']}")
        print("=" * 70)

        print(page["text"])