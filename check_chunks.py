import json


with open("data/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)


for chunk in chunks:

    if chunk["page"] == 6:

        print("=" * 70)
        print(chunk["chunk_id"])
        print("=" * 70)

        print(chunk["text"])