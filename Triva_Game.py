"""
    trivia_game.py
    Gabby, Abir, Roland

    A multiple-choice trivia game. The player is shown a question and a set
    of lettered choices, types the letter of their answer, and the game
    keeps track of how many they got right.
"""

questions: list[dict] = [
    {
        "question": "What is the capital of France?",
        "choices": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"], 
        "answer": "C",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B",
    },
    {
        "question": "What is the chemical compoound for the element gold?",
        "choices": ["A) Go", "B) Gd", "C) Ag", "D) Au"],
        "answer": "D",
    }
    {
        "question": "Which river is widely recognized as the longest river in the world?",
        "choices": ["A) Nile River", "B) Amazon River", "C) Yangtze River", "D) Mississippi River"],
        "answer": "A",
    }
    {
        "question": "Which cellular organelle is famously known as the ""powehouse of the cell""?",
        "choices": ["A) Nucleus", "B) Ribosome", "C) Mitochondria", "D) Endoplasmic reticulum"],
        "answer": "C",
    }
    {
        "question": "Which physicist revolutionized modern physics with the publication of theory of general relativity in 1915?",
        "choices": ["A) Albert Einstein", "B) Isaac Newton", "C) Niels Bohr", "D) Henri Matisse"],
        "answer": "A",
    }
]

print("+-----------------------------------------------------------------+")
print("|                    Welcome to the Trivia Game!                  |")
print("| Answer each question by typing the letter of your choice.       |")
print("+-----------------------------------------------------------------+")
print()

score: int = 0
index: int = 0

while index < len(questions):
    current_question = questions[index]

    print(f"Question {index + 1}: {current_question['question']}")

    choice_index = 0
    while choice_index < len(current_question["choices"]):
        print(current_question["choices"][choice_index])
        choice_index += 1

    answer = input("Your answer (just the letter): ").strip().upper()

    if answer == current_question["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Sorry, the correct answer was {current_question['answer']}.")

    print()
    index += 1

print("+-----------------------------------------------------------------+")
print(f"You scored {score} out of {len(questions)}!")
print("+-----------------------------------------------------------------+")
