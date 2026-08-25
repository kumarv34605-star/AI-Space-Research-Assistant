from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Apollo spacecraft used a service propulsion system.",
    "The spacecraft required propulsion for orbital maneuvers.",
    "Python is a programming language.",
    "The International Space Station operates in low Earth orbit.",
]

def search(question, documents, top_k = 2):
    document_embeddings = model.encode(documents)
    question_embedding = model.encode([question])

    scores = cosine_similarity(
        question_embedding,
        document_embeddings
    )[0]
    results = list(zip(documents, scores))
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:top_k]

question = "What propulsion system was used by the Apollo spacecraft?"
results = search(question, documents)

for document, score in results:
    print(f"{score:.4f}  →  {document}")