import json
import chromadb
from sentence_transformers import SentenceTransformer


## Load embedding model

model = SentenceTransformer("all-MiniLM-L6-v2")

## Load structured chunks from JSON file

with open("data/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)
    
## Create/ open persistent ChromaDB collection

client = chromadb.PersistentClient(
    path="./chroma_db"
)

## Create/ get our collection

collection = client.get_or_create_collection(
    name="space_documents"
)
## Extract data from chunks

ids = [chunk["chunk_id"] for chunk in chunks]

documents = [chunk["text"] for chunk in chunks]

metadatas = [
    {
        "page" : chunk["page"],
        "source": chunk["source"]
    }
    for chunk in chunks
]

## Generate embeddings for the documents
embeddings = model.encode(documents)

## store everything in chromadb

collection.add(
    ids = ids,
    documents = documents,
    metadatas = metadatas,
    embeddings = embeddings.tolist()
)

## Verify 

print("Ingestion Complete!")
print("Number of chunks stored:", collection.count())