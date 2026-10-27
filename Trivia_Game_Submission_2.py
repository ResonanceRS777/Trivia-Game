"""
trivia_game.py
Roland, Gabby, Abir

A multiple-choice trivia game. The player picks a category and a difficulty,
is shown the matching questions in a random order, types the letter of their
answer to each one, and the game keeps track of how many they got right.
"""


# This is the full set of trivia questions. It's a LIST of DICTIONARIES: each
# each item in the list is one question, and each question is a dictionary
# that bundles together everything that question needs.

questions: list[dict[str, str | list[str]]] = [
    {
        "question": "What is the capital of France?", # "question" -> the text shown to the player.
        "choices": [ # "choices" -> the list of choices shown to the player.
            "A) Berlin",
            "B) Madrid",
            "C) Paris",
            "D) Rome"
        ],
        "answer": "C", # "answer" -> the correct answer.
        "category": "Geography", # "category" -> the topic the question belongs to.
        "difficulty": "Easy", # "difficult" -> "Easy", "Medium" or "Hard"
    },
    {
        "question": "How many continents are there?",
        "choices": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8"
        ],
        "answer": "C",
        "category": "Geography",
        "difficulty": "Easy",
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "choices": [
            "A) Atlantic Ocean",
            "B) Pacific Ocean",
            "C) Indian Ocean",
            "D) Arctic Ocean",
        ],
        "answer": "B",
        "category": "Geography",
        "difficulty": "Easy",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": [
            "A) Venus",
            "B) Mars",
            "C) Jupiter",
            "D) Saturn"
            ],
        "answer": "B",
        "category": "Science",
        "difficulty": "Easy",
    },
    {
        "question": "What does CPU stand for?",
        "choices": [
            "A) Central Processing Unit",
            "B) Computer Personal Unit",
            "C) Central Program Utility",
            "D) Core Processing Unit",
        ],
        "answer": "A",
        "category": "Technology",
        "difficulty": "Easy",
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": [
            "A) Go",
            "B) Gd",
            "C) Ag",
            "D) Au"
        ],
        "answer": "D",
        "category": "Science",
        "difficulty": "Easy",
    },
    {
        "question": "Which river is widely recognized as the longest river in the world?",
        "choices": [
            "A) Nile River",
            "B) Amazon River",
            "C) Yangtze River",
            "D) Mississippi River",
        ],
        "answer": "A",
        "category": "Geography",
        "difficulty": "Easy",
    },
    {
        "question": 'Which cellular organelle is famously known as the "powerhouse of the cell"?',
        "choices": [
            "A) Nucleus",
            "B) Ribosome",
            "C) Mitochondria",
            "D) Endoplasmic reticulum",
        ],
        "answer": "C",
        "category": "Science",
        "difficulty": "Easy",
    },
    {
        "question": (
            "Which physicist revolutionized modern physics with the publication "
            "of the theory of general relativity in 1915?"
        ),
        "choices": [
            "A) Albert Einstein",
            "B) Isaac Newton",
            "C) Niels Bohr",
            "D) Henri Matisse",
        ],
        "answer": "A",
        "category": "Science",
        "difficulty": "Easy",
    },
]

category_options: list[str] = [
    "Geography",
    "Science",
    "Technology",
    "All Categories",
]
difficulty_options: list[str] = [
    "Easy",
    "Medium",
    "Hard",
    "All difficulties"
]


# This function displays a numbered menu and lets the player choose an option.
# It returns the text of the selected option as a string.
def choose_from_menu(title: str, options: list[str]) -> str:
    print(title)

    # valid_numbers holds the menu numbers the player is allowed to type.
    valid_numbers: list[str] = []

    # Loop through every option using its index (position).
    for position in range(len(options)):
        print(f"    {position + 1}) {options[position]}") # Display the current option with its corresponding menu number.
        valid_numbers.append(str(position + 1)) # Convert the displayed menu number into a string. Add it to valid_numbers.

    choice: str = input("Your choice (number): ").strip() # Asks the player to enter the number of their desired option.

    # Keep re-asking until the player types one of the real menu numbers.
    while choice not in valid_numbers:
        print(
            f"'{choice}' isn't one of the options. "
            f"Please enter one of: {', '.join(valid_numbers)}"
        )
        choice = input("Your choice (number): ").strip() 

    # The menu starts at 1 but list indexes start at 0, so subtract 1.
    return options[int(choice) - 1]

play_again: str = "Y"

while play_again == "Y":

    print("+-----------------------------------------------------------------+")
    print("|                    Welcome to the Trivia Game!                  |")
    print("| Answer each question by typing the letter of your choice.       |")
    print("+-----------------------------------------------------------------+")
    print()

    category: str = choose_from_menu("Choose a category:", category_options)
    print()
    difficulty: str = choose_from_menu(
        "Choose a difficulty", difficulty_options
    )
    print()

    score: int = 0  # score  -> counts how many questions the player has gotten right so far.
    index: int = 0  # index  -> tracks which question in the "questions" list we're currently on.

    # Keep only the questions that match the selected category and difficulty.
    question_pool: list[dict[str, str | list[str]]] = []

    while index < len(questions): # Outer loop: runs once per question. It keeps going as long as there are still questions left to ask
        current_question = questions[index] # Pull out the single dictionary for whichever question the player is on right now, giving easy access to the "question", "choices", and "answer" values.

        print(f"Question {index + 1}: {current_question['question']}") # Show the question text. index + 1 is just for display, so the player

        choice_index = 0
        while choice_index < len(current_question["choices"]): # Inner loop: runs once per choice for the current question. It keeps going as long as there are choices left to show.
            print(current_question["choices"][choice_index]) # Show the choice text. The choices are already lettered, so we don't need to add letters here.
            choice_index += 1 # Increment the choice_index so we can move on to the next choice in the next iteration of this inner loop.

        valid_letters = [choice[0] for choice in current_question["choices"]] # ["A", "B", "C", "D"] pulled from "A) Berlin", etc.

        answer = input("Your answer (just the letter): ").strip().upper()
        while answer not in valid_letters: # Keep re-asking until they actually type one of the real choices.
            print(f"'{answer}' isn't one of the choices. Please enter one of: {', '.join(valid_letters)}")
            answer = input("Your answer (just the letter): ").strip().upper()

        if answer == current_question["answer"]: # If the player's answer matches the correct answer for this question, they got it right.
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer was {current_question['answer']}.")

        print()
        index += 1

    print("+-----------------------------------------------------------------+")
    print(f"You scored {score} out of {len(questions)}!") # Displays the final score.

    if score == 0:
        print("When your parents dropped you off at the bus stop, did you even get on?")

    if score == len(questions):
        print("You got the perfect score!")

    elif score > 0 and score < len(questions):
        print("You could've done better, but at least you did better than zero.")

    print("+-----------------------------------------------------------------+")
    print()

    play_again = input("Do you want to play again? (Y/N): ").strip().upper() # Ask the player if they want another round. Anything other than "Y" ends the outer loop.
    print()

print("Thanks for playing!")
