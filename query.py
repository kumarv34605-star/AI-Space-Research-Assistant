import chromadb
from sentence_transformers import SentenceTransformer


# Load the same embedding model used during ingestion
model = SentenceTransformer("all-MiniLM-L6-v2")


# Open the persistent ChromaDB
client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="space_documents"
)

## Users question 
query = "What is the nominal thrust of the Service Module engine?"

## Convert question into an embedding
query_embedding = model.encode(query)

## Search chromadb
results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=3
)

## Display results
print("\nQuery:")
print(query)
print("\n--- Retrieved Chunks ---")

for i in range(len(results["documents"][0])):

    print(f"\nResult {i + 1}")
    print("Distance:", results["distances"][0][i])
    print("Page:", results["metadatas"][0][i]["page"])
    print("Source:", results["metadatas"][0][i]["source"])
    print("Text:", results["documents"][0][i])