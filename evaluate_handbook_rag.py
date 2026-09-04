from rag import answer_question


questions = [
    "What is systems engineering?",
    "What is verification?",
    "What is validation?",
    "What is risk management?",
    "What is the purpose of technical reviews?",
    "What are the major steps in the validation process?",
    "What is the difference between verification and validation?",
    "What is Risk-Informed Decision Making?",
    "What is Continuous Risk Management?",
    "What is the nominal thrust of the Apollo Service Module engine?",
]


for i, question in enumerate(questions, start=1):

    print("\n" + "=" * 80)
    print(f"QUESTION {i}")
    print("=" * 80)
    print(question)

    try:
        answer, results = answer_question(question)

        print("\nANSWER")
        print("-" * 80)
        print(answer)

        print("\nSOURCES")
        print("-" * 80)

        for result in results:
            print(
                f"Page {result['page']} | "
                f"Distance {result['distance']:.4f}"
            )

    except Exception as e:
        print(f"\nERROR: {e}")