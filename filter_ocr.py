import json
import re


INPUT_PATH = "data/ocr_pages.json"
OUTPUT_PATH = "data/filtered_ocr_pages.json"


def is_meaningful_text(text):
    """
    Basic heuristic for deciding whether OCR output
    contains useful textual content.
    """

    if not text:
        return False

    text = text.strip()

    words = re.findall(r"\b[a-zA-Z]{2,}\b", text)

    # Very short text may still be useful if it
    # looks like a figure or table caption.
    if len(text) < 80:

        caption_words = [
            "figure",
            "table",
            "fig.",
            "figure."
        ]

        if not any(word in text.lower() for word in caption_words):
            return False

    # For normal text, require a reasonable number of words.
    if len(text) >= 80 and len(words) < 10:
        return False

    # Ratio of alphabetic characters
    letters = sum(char.isalpha() for char in text)

    if letters / len(text) < 0.50:
        return False

    return True


with open(INPUT_PATH, "r", encoding="utf-8") as f:
    pages = json.load(f)


filtered_pages = []

for page in pages:

    if is_meaningful_text(page["text"]):
        filtered_pages.append(page)


with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(
        filtered_pages,
        f,
        ensure_ascii=False,
        indent=2
    )


print(f"Original pages: {len(pages)}")
print(f"Kept pages: {len(filtered_pages)}")
print(f"Removed pages: {len(pages) - len(filtered_pages)}")
print(f"Saved to {OUTPUT_PATH}")