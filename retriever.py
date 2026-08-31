import chromadb
from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"


model = SentenceTransformer(MODEL_NAME)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="space_documents"
)


def retrieve(query, n_results=3):

    query_embedding = model.encode(query)

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
    )

    retrieved_chunks = []

    for i in range(len(results["documents"][0])):

        retrieved_chunks.append({
            "text": results["documents"][0][i],
            "page": results["metadatas"][0][i]["page"],
            "source": results["metadatas"][0][i]["source"],
            "distance": results["distances"][0][i]
        })

    return retrieved_chunks

if __name__ == "__main__":

    results = retrieve(
        "What is the nominal thrust of the Service Module engine?"
    )

    for result in results:
        print("\nPage:", result["page"])
        print("Distance:", result["distance"])
        print("Text:", result["text"])