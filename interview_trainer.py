role = input("Enter Job Role: ").lower()

questions = {
    "software engineer": [
        "Explain OOP concepts.",
        "What is normalization in DBMS?",
        "Difference between process and thread?",
        "What is polymorphism?",
        "Explain inheritance."
    ],

    "data scientist": [
        "What is machine learning?",
        "Difference between supervised and unsupervised learning?",
        "What is overfitting?",
        "Explain regression.",
        "What is feature engineering?"
    ],

    "ai engineer": [
        "What is RAG?",
        "Explain embeddings.",
        "What is LangChain?",
        "What are vector databases?",
        "What is Agentic AI?"
    ]
}

print("\n==============================")
print("INTERVIEWACE AI")
print("==============================")

if role in questions:
    print("\nTechnical Questions:\n")

    for i, q in enumerate(questions[role], start=1):
        print(f"{i}. {q}")

else:
    print("\nRole not found.")