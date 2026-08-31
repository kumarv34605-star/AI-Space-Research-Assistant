import json
from pathlib import Path
import re


def split_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]


def chunk_text(text, chunk_size=500, overlap_sentences=1):
    sentences = split_sentences(text)

    chunks = []
    current_sentences = []

    for sentence in sentences:

        current_length = sum(
            len(s) for s in current_sentences
        )

        if current_length + len(sentence) <= chunk_size:
            current_sentences.append(sentence)

        else:
            if current_sentences:
                chunks.append(" ".join(current_sentences))

            # Keep the last few sentences for overlap
            current_sentences = current_sentences[
                -overlap_sentences:
            ]

            current_sentences.append(sentence)

    if current_sentences:
        chunks.append(" ".join(current_sentences))

    return chunks


# Load cleaned OCR pages
with open("data/cleaned_ocr_pages.json", "r", encoding="utf-8") as f:
    pages = json.load(f)


all_chunks = []


for page in pages:

    page_number = page["page"]
    source = page["source"]
    text = page["text"]

    chunks = chunk_text(text)

    for chunk_number, chunk in enumerate(chunks, start=1):

        all_chunks.append({
            "chunk_id": f"page_{page_number}_chunk_{chunk_number}",
            "page": page_number,
            "source": source,
            "text": chunk
        })


# Save chunks
Path("data").mkdir(exist_ok=True)

with open("data/chunks.json", "w", encoding="utf-8") as f:
    json.dump(
        all_chunks,
        f,
        indent=2,
        ensure_ascii=False
    )


print(f"Total chunks: {len(all_chunks)}")
print("Saved to data/chunks.json")

print("\n--- FIRST 5 CHUNKS ---")

for chunk in all_chunks[:5]:
    print(f"\nID: {chunk['chunk_id']}")
    print(f"Page: {chunk['page']}")
    print(f"Source: {chunk['source']}")
    print(f"Text: {chunk['text']}")