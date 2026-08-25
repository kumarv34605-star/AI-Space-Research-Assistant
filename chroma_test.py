import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="space_documents"
)

documents = [
    "Apollo spacecraft used a service propulsion system.",
    "The spacecraft required propulsion for orbital maneuvers.",
    "Python is a programming language.",
    "The International Space Station operates in low Earth orbit.",
]

ids = [
    "doc1",
    "doc2",
    "doc3",
    "doc4",
]

collection.add(
    documents=documents,
    ids=ids,
)

print("Documents added!")

results = collection.query(
    query_texts= [
        "What propulsion system did the Apollo spacecraft use?"
    ],
    n_results=2,
)

print(results)