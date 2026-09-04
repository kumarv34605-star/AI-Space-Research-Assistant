import chromadb
from sentence_transformers import SentenceTransformer


# Load the same embedding model used during ingestion
model = SentenceTransformer("all-MiniLM-L6-v2")


# Open persistent ChromaDB
client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="space_documents"
)


def retrieve(question, top_k=5):
    """
    Retrieve the most relevant chunks for a question.
    """

    # Convert the question into an embedding
    query_embedding = model.encode(question)

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
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

    question = "What is the purpose of technical reviews?"

    results = retrieve(question, top_k=5)

    for result in results:

        print(f"\nPage: {result['page']}")
        print(f"Distance: {result['distance']}")
        print(f"Text: {result['text']}")