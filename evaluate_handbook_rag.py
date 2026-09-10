from rag import answer_question


evaluation_questions = [
    {
        "question": "What is systems engineering?",
        "expected": [
            "methodical",
            "multi-disciplinary",
            "system",
            "requirements"
        ],
        "expected_pages":[13],
        "answerable": True
    },
    {
        "question": "What is verification?",
        "expected": [
            "specified requirements",
            "test",
            "analysis",
            "inspection"
        ],
        "expected_pages":[100],
        "answerable": True
    },
    {
        "question": "What is validation?",
        "expected": [
            "stakeholder",
            "expectations"
        ],
        "expected_pages":[110],
        "answerable": True
    },
    {
        "question": "What is risk management?",
        "expected": [
            "risk",
            "mitigat"
        ],
        "expected_pages":[152],
        "answerable": True
    },
    {
        "question": "What is the purpose of technical reviews?",
        "expected": [
            "management",
            "decision",
            "readiness"
        ],
        "expected_pages":[170],
        "answerable": True
    },
    {
        "question": "What are the major steps in the validation process?",
        "expected": [
            "preparing validation",
            "performing validation",
            "analyzing results",
            "validation report",
            "work products"
        ],
        "expected_pages":[110],
        "answerable": True
    },
    {
        "question": "What is the difference between verification and validation?",
        "expected": [
            "verification",
            "validation",
            "requirements",
            "realistic"
        ],
        "expected_pages":[99, 100, 109, 110],
        "answerable": True
    },
    {
        "question": "What is Risk-Informed Decision Making?",
        "expected": [
            "risk",
            "decision",
            "stakeholders"
        ],
        "expected_pages": [152, 200],
        "answerable": True
    },
    {
        "question": "What is Continuous Risk Management?",
        "expected": [
            "continuous",
            "risk",
            "life cycle"
        ],
        "expected_pages":[152],
        "answerable": True
    },
    {
        "question": "What is the nominal thrust of the Apollo Service Module engine?",
        "expected": [
            "information is not available"
        ],
        "answerable": False
    }
]


total_questions = len(evaluation_questions)

answerable_questions = 0
answerable_passed = 0

retrieval_passed = 0

unsupported_questions = 0
unsupported_correctly_rejected = 0


for i, item in enumerate(evaluation_questions, start=1):

    question = item["question"]
    expected_terms = item["expected"]
    expected_pages = item.get("expected_pages", [])
    answerable = item["answerable"]

    print("\n" + "=" * 80)
    print(f"QUESTION {i}")
    print("=" * 80)
    print(question)

    try:

        answer, results = answer_question(question)

        answer_lower = answer.lower()

        matched_terms = []

        for term in expected_terms:
            term_lower = term.lower()

            # Exact phrase match
            if term_lower in answer_lower:
                matched_terms.append(term)
                continue

            # Match important words from the expected concept
            words = term_lower.split()

            if len(words) > 1:
                matched_words = sum(
                    word in answer_lower
                    for word in words
                )

                if matched_words / len(words) >= 0.75:
                    matched_terms.append(term)

        score = len(matched_terms) / len(expected_terms)
        
        retrieved_pages = [
            result["page"]
            for result in results
        ]

        retrieval_match = any(
            page in retrieved_pages
            for page in expected_pages
        )

        print("\nANSWER")
        print("-" * 80)
        print(answer)

        print("\nEVALUATION")
        print("-" * 80)

        print(f"Matched: {matched_terms}")
        print(f"Score: {score:.0%}")
        
        print(f"Retrieved pages: {retrieved_pages}")
        print(f"Expected pages: {expected_pages}")

        if answerable:
            if retrieval_match:
                print("Retrieval: PASS")
                retrieval_passed += 1
            else:
                print("Retrieval: REVIEW")

        if answerable:

            answerable_questions += 1

            if score >= 0.75:
                print("RESULT: PASS")
                answerable_passed += 1
            else:
                print("RESULT: REVIEW")

        else:

            unsupported_questions += 1

            refusal_phrase = "information is not available"

            if refusal_phrase in answer_lower:
                print("RESULT: CORRECTLY REJECTED")
                unsupported_correctly_rejected += 1
            else:
                print("RESULT: HALLUCINATION RISK")

        print("\nSOURCES")
        print("-" * 80)

        for result in results:

            print(
                f"Page {result['page']} | "
                f"Distance {result['distance']:.4f}"
            )

    except Exception as e:

        print(f"\nERROR: {e}")


print("\n" + "=" * 80)
print("RAG EVALUATION SUMMARY")
print("=" * 80)

print(f"Total questions: {total_questions}")
print(f"Answerable questions: {answerable_questions}")
print(f"Answerable questions passed: {answerable_passed}")

if answerable_questions > 0:
    answerable_score = answerable_passed / answerable_questions
    print(f"Answerable question score: {answerable_score:.0%}")
    
if answerable_questions > 0:
    retrieval_score = retrieval_passed / answerable_questions
    print(f"Retrieval quality score: {retrieval_score:.0%}")

print(
    f"\nUnsupported questions: "
    f"{unsupported_questions}"
)

print(
    f"Unsupported questions correctly rejected: "
    f"{unsupported_correctly_rejected}"
)

if unsupported_questions > 0:
    refusal_score = (
        unsupported_correctly_rejected /
        unsupported_questions
    )
    print(
        f"Unsupported-question rejection score: "
        f"{refusal_score:.0%}"
    )