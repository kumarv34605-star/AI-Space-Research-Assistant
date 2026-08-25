import json

def chunk_test(text, chunk_size=500, overlap=100):
    chunks = []
    
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        
        chunk = text[start:end]
        chunks.append(chunk)
        
        start = end - overlap  # Move start back by overlap for the next chunk
    
    return chunks

## Load extracted pages 
with open("data/extracted_pages.json", "r", encoding="utf-8") as f:
    pages = json.load(f)
    
## Try it on page 6

page = pages[5]

chunks = chunk_test(page["text"])

print("Page:", page["page"])
print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks, start=1):
    print(f"\n-- CHUNK {i} --")
    print(chunk)