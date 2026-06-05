role = input("Enter Job Role: ")

print("\n================================")
print("INTERVIEWACE AI")
print("================================")

if role.lower() == "software engineer":

    technical = [
        "Explain OOP concepts.",
        "Difference between process and thread?",
        "What is normalization in DBMS?",
        "Explain polymorphism.",
        "What is a primary key?"
    ]

elif role.lower() == "data scientist":

    technical = [
        "What is Machine Learning?",
        "Difference between supervised and unsupervised learning?",
        "What is overfitting?",
        "Explain Linear Regression.",
        "What is a confusion matrix?"
    ]

elif role.lower() == "web developer":

    technical = [
        "What is HTML?",
        "Difference between GET and POST?",
        "Explain CSS Flexbox.",
        "What is JavaScript?",
        "What is REST API?"
    ]

else:

    technical = [
        "Tell us about your technical skills.",
        "Describe your latest project.",
        "What programming languages do you know?"
    ]

print("\nRole Selected:", role)

print("\nTechnical Questions:")

for i, q in enumerate(technical, start=1):
    print(f"{i}. {q}")

print("\nHR Questions:")

hr = [
    "Tell me about yourself.",
    "Why should we hire you?",
    "What are your strengths?",
    "Where do you see yourself in 5 years?",
    "Describe a challenge you faced."
]

for i, q in enumerate(hr, start=1):
    print(f"{i}. {q}")

print("\nInterview Ready Score: 8/10")
print("Suggestion: Improve communication and project explanation skills.")