import json
import chromadb
from sentence_transformers import SentenceTransformer

INPUT_PATH = "data/handbook_chunks.json"
CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "space_documents"

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading chunks...")
with open(INPUT_PATH, "r", encoding="utf-8") as f:
    chunks = json.load(f)

print(f"Loaded {len(chunks)} chunks.")

client = chromadb.PersistentClient(path=CHROMA_PATH)

# Delete old collection if it exists
try:
    client.delete_collection(name=COLLECTION_NAME)
    print("Deleted old collection.")
except Exception:
    pass

collection = client.create_collection(name=COLLECTION_NAME)

print("Creating embeddings...")

texts = [chunk["text"] for chunk in chunks]

embeddings = model.encode(
    texts,
    show_progress_bar=True
)

print("Adding documents to ChromaDB...")

collection.add(
    ids=[chunk["id"] for chunk in chunks],
    documents=texts,
    embeddings=embeddings.tolist(),
    metadatas=[
        {
            "source": chunk["source"],
            "page": chunk["page"]
        }
        for chunk in chunks
    ]
)

print("\nIngestion complete.")
print(f"Total documents in ChromaDB: {collection.count()}")