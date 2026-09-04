from retriever import retrieve
from generator import generate_answer


def build_context(results):
    """
    Convert retrieved chunks into a single context string.
    """

    context_parts = []

    for result in results:

        context_parts.append(
            f"[Source: {result['source']}, Page: {result['page']}]\n"
            f"{result['text']}"
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

    question = "What is systems engineering?"

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