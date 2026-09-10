import os
import requests

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)
MODEL = "qwen3:1.7b"


def generate_answer(question, context):
    prompt = f"""
    Answer the question using only the context below.

    Context:
    {context}

    Question:
    {question}

    If the context contains the answer, answer directly.
    If it does not contain the answer, say:
    "The information is not available in the provided context."

    Answer:
    """

    response = requests.post(
    OLLAMA_URL,
    json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0
        }
    }
)

    response.raise_for_status()

    data = response.json()

    return data["response"]


if __name__ == "__main__":

    question = "What is the nominal thrust of the Service Module engine?"

    context = """
    The service module engine has a nominal thrust of
    21 500 pounds and is used for midcourse correction
    during the translunar phase, lunar orbit insertion,
    transearth injection, and midcourse correction during
    the transearth phase.
    """

    answer = generate_answer(question, context)

    print("\nQuestion:")
    print(question)

    print("\nAnswer:")
    print(answer)