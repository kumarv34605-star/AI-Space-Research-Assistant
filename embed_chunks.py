import json
from sentence_transformers import SentenceTransformer

##Load embedding model
model = SentenceTransformer("all-miniLM-L6-v2")

## load chunks
with open("data/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)
    
##extract the text only
texts = [chunk["text"] for chunk in chunks]

## Generate embeddings

embeddings = model.encode(texts)

print("Number of chunks:", len(chunks))
print("Embeddings matrix shape:",embeddings.shape)
print("First vector size:", len(embeddings[0]))
print("First 5 values", embeddings[0][:5])