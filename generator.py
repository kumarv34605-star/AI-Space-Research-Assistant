import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:1.7b"


def generate_answer(question, context):
    prompt = f"""
You are a research assistant answering questions about the provided document.

RULES:
1. Answer using ONLY the provided context.
2. Do not add facts from your own knowledge.
3. Do not invent or expand abbreviations unless the context explicitly defines them.
4. Preserve the terminology used in the context.
5. If the context does not contain enough information, say:
   "The information is not available in the provided context."
6. Give a concise, direct answer.
7. When comparing concepts, clearly separate the concepts and only state
   differences supported by the context.

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