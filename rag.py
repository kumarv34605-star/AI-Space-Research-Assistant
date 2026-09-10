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


RELEVANCE_THRESHOLD = 1.0


def answer_question(question):

    # 1. Retrieve relevant chunks
    results = retrieve(question, top_k=5)

    # 2. Check whether the best retrieved chunk is relevant enough
    best_distance = results[0]["distance"]

    if best_distance > RELEVANCE_THRESHOLD:
        answer = (
            "The information is not available in the provided context."
        )
        return answer, []

    # 3. Build context for the LLM
    context = build_context(results)
    
    

    # 4. Generate answer using the retrieved context
    answer = generate_answer(
        question,
        context
    )

    source_pages = sorted(
        set(result["page"] for result in results)
    )

    citation = " [Pages " + ", ".join(map(str, source_pages)) + "]"

    answer = answer.strip() + citation

    return answer, results


if __name__ == "__main__":

    
    question = "What is Risk-Informed Decision Making?"
    #question = "What is systems engineering?"
    #question = "What is the difference between verification and validation?"
    #question = "What is the nominal thrust of the Apollo Service Module engine?"
    #question = "What is verification?"
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