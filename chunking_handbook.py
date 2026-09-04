import json
import re


INPUT_PATH = "data/handbook_pages.json"
OUTPUT_PATH = "data/handbook_chunks.json"

CHUNK_SIZE = 1000
OVERLAP = 200


def split_into_chunks(text):
    sentences = re.split(r"(?<=[.!?])\s+", text)

    chunks = []
    current = ""

    for sentence in sentences:

        if len(current) + len(sentence) + 1 <= CHUNK_SIZE:
            current += (" " if current else "") + sentence

        else:
            if current:
                chunks.append(current)

            overlap_text = current[-OVERLAP:] if current else ""
            current = overlap_text + " " + sentence

    if current:
        chunks.append(current)

    return chunks


with open(INPUT_PATH, "r", encoding="utf-8") as f:
    pages = json.load(f)


chunks = []

for page in pages:

    text = page["text"]

    if not text:
        continue

    page_chunks = split_into_chunks(text)

    for i, chunk in enumerate(page_chunks, start=1):

        chunks.append({
            "id": f"page_{page['page']}_chunk_{i}",
            "source": page["source"],
            "page": page["page"],
            "text": chunk
        })


with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=2, ensure_ascii=False)


print(f"Created {len(chunks)} chunks.")
print(f"Saved to: {OUTPUT_PATH}")