from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Apollo spacecraft used a service propulsion system.",
    "The spacecraft required propulsion for orbital maneuvers.",
    "Python is a programming language.",
    "The International Space Station operates in low Earth orbit.",
]

question = "What propulsion system was used by the Apollo spacecraft?"

document_embeddings = model.encode(documents)
question_embedding = model.encode([question])

scores = cosine_similarity(
    question_embedding,
    document_embeddings
)[0]

for document, score in zip(documents, scores):
    print(f"{score:.4f}  →  {document}")