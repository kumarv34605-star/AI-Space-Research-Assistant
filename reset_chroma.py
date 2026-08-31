import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection_name = "space_documents"

try:
    client.delete_collection(collection_name)
    print(f"Deleted collection: {collection_name}")
    
except Exception:
    print(f"Collection '{collection_name}' does not exist or could not be deleted.")
    
collection = client.get_or_create_collection(
    name=collection_name
)
print(f"Created collection: {collection_name}")
print("Number of chunks:", collection.count())