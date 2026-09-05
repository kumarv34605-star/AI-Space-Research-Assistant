from retriever import retrieve
from generator import generate_answer


def build_context(results):
    context_parts = []
    seen_texts = set()

    for result in results:
        text = result["text"].strip()

        if text in seen_texts:
            continue

        seen_texts.add(text)

        context_parts.append(
            f"[Source: {result['source']}, Page: {result['page']}]\n"
            f"{text}"
        )

    return "\n\n".join(context_parts)


def answer_question(question):

    # 1. Retrieve relevant chunks
    results = retrieve(question, top_k=5)

    # 2. Build context for the LLM
    context = build_context(results)

    # 3. Generate answer using the retrieved context
    answer = generate_answer(
        question,
        context
    )

    return answer, results


if __name__ == "__main__":

    #question = "What is systems engineering?"
    question = "What is the difference between verification and validation?"
    answer, results = answer_question(question)

    print("\n" + "=" * 70)
    print("QUESTION")
    print("=" * 70)
    print(question)

    print("\n" + "=" * 70)
    print("ANSWER")
    print("=" * 70)
    print(answer)

    print("\n" + "=" * 70)
    print("SOURCES")
    print("=" * 70)

    for result in results:

        print(
            f"- {result['source']} | "
            f"Page {result['page']} | "
            f"Distance {result['distance']:.4f}"
        )