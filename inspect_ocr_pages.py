import json


with open("data/ocr_pages.json", "r", encoding="utf-8") as f:
    pages = json.load(f)


pages_to_inspect = [12, 18, 20, 25, 26, 30, 34, 42]


for page in pages:

    if page["page"] in pages_to_inspect:

        print("\n" + "=" * 70)
        print(f"PAGE {page['page']}")
        print("=" * 70)

        print(page["text"])