#Quiz game with programming questions

#Q&A
info = [
    {
        "question": "¿Which is not a programming language?",
        "choices": ["Python", "CSS", "PHP", "Javascript", "R"],
        "answer": 2,
    },

    {
        "question": "¿Which is not a code editor?",
        "choices": ["Visual studio", "Sublime text", "Vim", "Word", "Atom"],
        "answer": 4,
    },
    {
        "question": "¿Which is the javacript extension?",
        "choices": [".jp", ".js", ".jc", ".ji", ".ja"],
        "answer": 2,
    },

    {
        "question": "¿Which is not a framework?",
        "choices": ["React", "Vue", "Tailwind", "Angular", "Kotlin"],
        "answer": 5,
    },

    {
        "question": "¿Which language has an animal in its logo?",
        "choices": ["C#", "Java", "C++", "Python", "PHP"],
        "answer": 4,
    }
]

#Score
score = 0

for i in range(len(info)):
    questions = info[i]["question"]
    options = info[i]["choices"]
    answers = info[i]["answer"]
    print(questions)
    for n,j in enumerate(options):
        print(f"{n+1} - {j}")
    user = int(input("Your answer: "))
    if user == answers:
        score += 1

print(f"Final score: {score}")
