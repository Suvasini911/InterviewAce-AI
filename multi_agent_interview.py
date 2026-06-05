print("===================================")
print("      INTERVIEWACE AI")
print("===================================")

name = input("Enter your name: ")
role = input("Enter job role: ")

print("\nHello", name)
print("Preparing interview for:", role)

# Agent 1: Resume Analysis Agent
print("\n[Resume Analysis Agent]")
skills = input("Enter your skills (comma separated): ")

# Agent 2: Technical Question Agent
print("\n[Technical Question Agent]")

technical_questions = [
    "Explain OOP concepts.",
    "What is polymorphism?",
    "Difference between process and thread?",
    "What is normalization in DBMS?",
    "Explain REST API."
]

for i, q in enumerate(technical_questions, start=1):
    print(f"{i}. {q}")

# Agent 3: HR Agent
print("\n[HR Interview Agent]")

hr_questions = [
    "Tell me about yourself.",
    "Why should we hire you?",
    "What are your strengths?",
    "Where do you see yourself in 5 years?"
]

for i, q in enumerate(hr_questions, start=1):
    print(f"{i}. {q}")

# Agent 4: Feedback Agent
print("\n[Feedback Agent]")
score = 8

print("Confidence Score:", score, "/10")

print("\nSuggestions:")
print("- Improve communication skills")
print("- Mention projects clearly")
print("- Practice technical concepts")