import json


with open("data/ocr_pages.json", "r", encoding="utf-8") as f:
    pages = json.load(f)


for page in pages:

    text = page["text"]

    print(
        f"Page {page['page']:>2} | "
        f"Characters: {len(text):>5}"
    )