import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:1.7b"


def generate_answer(question, context):
    prompt = f"""
You are a helpful research assistant.

Answer the user's question using ONLY the provided context.

If the context does not contain enough information to answer the question,
say that the information is not available in the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
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