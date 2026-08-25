from sentence_transformers import SentenceTransformer

## Load a pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding dimension:", 
      model.get_embedding_dimension())

sentences = [
    "Apollo spacecraft used a service propulsion system.",
    "The spacecraft required propulsion for orbital maneuvers.",
    "Python is a programming language.",
]

## Convert sentences into vectors
embeddings = model.encode(sentences)

for sentence, embedding in zip(sentences, embeddings):
    print(f"\nSentence: {sentence}")
    #print(f"Vector size: {len(embedding)}")
    print("Shape:", embedding.shape)
