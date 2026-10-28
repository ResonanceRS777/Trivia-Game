"""
trivia_game.py
Roland, Gabby, Abir

A multiple-choice trivia game. The player picks a category and a difficulty,
is shown the matching questions in a random order, types the letter of their
answer to each one, and the game keeps track of how many they got right.
"""

import random # Allows .randint importation. Gives the ability of for the questions to be randomized.
from pathlib import Path # Most efficient way of creating files on the user's computer.
from typing import cast # Pylance

# This is the full set of trivia questions. It's a LIST of DICTIONARIES: each
# each item in the list is one question, and each question is a dictionary
# that bundles together everything that question needs.

questions: list[dict[str, str | list[str]]] = [
    # ---------------------------- Geography ----------------------------
    {
        "question": "What is the capital of France?", # "question" -> the text shown to the player.
        "choices": [ # "choices" -> the list of choices shown to the player.
            "A) Berlin",
            "B) Madrid",
            "C) Paris",
            "D) Rome",
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
            "D) 8",
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
    "question": "Which river is widely recognized as the longest river in the world?",
    "choices": [
        "A) Nile River",
        "B) Amazon River",
        "C) Yangtze River",
        "D) Mississippi River",
        ],
        "answer": "A",
        "category": "Geography",
        "difficulty": "Medium",
    },
    {
        "question": "What is the capital of Australia?",
        "choices": [
            "A) Sydney",
            "B) Melbourne",
            "C) Camberra",
            "D) Perth",
        ],
        "answer": "C",
        "category": "Geography",
        "difficulty": "Medium",
    },
    {
        "question": "Which desert is the largest hot desert in the world?",
        "choices": [
            "A) Gobi Desert",
            "B) Sahara Desert",
            "C) Kalahari Desert",
            "D) Arabian Desert",
        ],
        "answer": "B",
        "category": "Geography",
        "difficulty": "Medium",
    },
    {
        "question": "Which mountain range is the longest on land?",
        "choices": [
            "A) Rocky Mountains",
            "B) Himalayas",
            "C) Andes",
            "D) Alps",
        ],
        "answer": "C",
        "category": "Geography",
        "difficulty": "Hard",
    },
    {
        "question": "Which two countries share the longest international border?",
        "choices": [
            "A) Russia and China",
            "B) Canada and the United States",
            "C) Argentina and Chile",
            "D) India and Pakistan",
        ],
        "answer": "B",
        "category": "Geography",
        "difficulty": "Hard",
    },
    {
        "question": "Which is the deepest lake in the world?",
        "choices": [
            "A) Lake Superior",
            "B) Lake Virtoria",
            "C) Lake Tanganyika",
            "D) Lake Bailkal",
        ],
        "answer": "D",
        "category": "Geography",
        "difficulty": "Hard",
    },
    # ---------------------------- Science ----------------------------
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": [
            "A) Venus",
            "B) Mars",
            "C) Jupiter",
            "D) Saturn",
        ],
        "answer": "B",
        "category": "Science",
        "difficulty": "Easy",
    },
    {
        "question": "Which gas do plants absorb from the air to make food during photosynthesis?",
        "choices": [
            "A) Oxygen",
            "B) Nitrogen",
            "C) Carbon dioxide",
            "D) Hydrogen",
        ],
        "answer": "C",
        "category": "Science",
        "difficulty": "Easy",
    },
    {
        "question": "At sea level, water boils at what temperature in degrees Celsius?",
        "choices": [
            "A) 90",
            "B) 100",
            "C) 212",
            "D) 50",
        ],
        "answer": "B",
        "category": "Science",
        "difficulty": "Easy",
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": [
            "A) Go",
            "B) Gd",
            "C) Ag",
            "D) Au",
        ],
        "answer": "D",
        "category": "Science",
        "difficulty": "Medium",
    },
    {
        "question": 'Which cellular organelle is famously known as the "powerhouse of the cell?"',
        "choices": [
            "A) Nucleus",
            "B) Ribosome",
            "C) Mitochondira",
            "D) Endoplasmic reticulum",
        ],
        "answer": "C",
        "category": "Science",
        "difficulty": "Medium",
    },
    {
        "question": "What is the most abundant gas in Earth's atmosphere?",
        "choices": [
            "A) Oxygen",
            "B) Hydrogen",
            "C) Carbon dioxide",
            "D) Argon",
        ],
        "answer": "B",
        "category": "Science",
        "difficulty": "Medium",
    },
    {
        "question": ("Which physicist revolutionized modern physics with the publication "
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
        "difficulty": "Hard",
    },
    {
        "question": "What is the most abundant element in the universe?",
        "choices": [
            "A) Helium",
            "B) Hydrogen",
            "C) Oxygen",
            "D) Carbon",
        ],
        "answer": "B",
        "category": "Science",
        "difficulty": "Hard",
    },
    {
        "question": "What is the SI unit of electrical resistance?",
        "choices": [
            "A) Volt",
            "B) Watt",
            "C) Ohm",
            "D) Ampere",
        ],
        "answer": "C",
        "category": "Science",
        "difficulty": "Hard",
    },
    # ---------------------------- Technology ----------------------------
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
        "question": "What does USB stand for?",
        "choices": [
            "A) United System Board",
            "B) Univeral Serial Bus",
            "C) Unified Software Backup",
            "D) Universal Storage Block"
        ],
        "answer": "B",
        "category": "Technology",
        "difficulty": "Easy",
    },
    {
        "question": 'What does the "www" in a website address stand for?',
        "choices": [
            "A) Wide World Web",
            "B) World Web Wide",
            "C) World Wide Web",
            "D) Web World Wide",
        ],
        "answer": "C",
        "category": "Technology",
        "difficulty": "Easy",
    },
    {
        "question": "What does HTML stand for?",
        "choices": [
            "A) High Transfer Markup Language",
            "B) HyperText Machine Language",
            "C) Home Tool Markup Language",
            "D) HyperText Markup Language",
        ],
        "answer": "D",
        "category": "Technology",
        "difficulty": "Medium",
    },
    {
        "question": "How many bits are in one byte?",
        "choices": [
            "A) 4",
            "B) 8",
            "C) 16",
            "D) 32",
        ],
        "answer": "B",
        "category": "Technology",
        "difficulty": "Medium",
    },
    {
        "question": "Which type of computer memory loses its contents when the power is turned off?",
        "choices": [
            "A) Hard disk",
            "B) SSD",
            "C) RAM",
            "D) USB flash drive",
        ],
        "answer": "C",
        "category": "Technology",
        "difficulty": "Medium",
    },
    {
        "question": "Who created the Python programming language?",
        "choices": [
            "A) Linus Torvalds",
            "B) Guido van Rossum",
            "C) James Gosling",
            "D) Bjarne Stroustrup",
        ],
        "answer": "B",
        "category": "Technology",
        "difficulty": "Hard",
    },
    {
        "question": "In networking, what does DNS stand for?",
        "choices": [
            "A) Digital Network Service",
            "B) Data Naming Standard",
            "C) Domain Name System",
            "D) Dynamic Node Server",
        ],
        "answer": "C",
        "category": "Technology",
        "difficulty": "Hard",
    },
    {
        "question": "What is the binary number 11010 equal to in decimal?",
        "choices": [
            "A) 22",
            "B) 26",
            "C) 28",
            "D) 30",
        ],
        "answer": "B",
        "category": "Technology",
        "difficulty": "Hard",
    },
]

# The final option in each menu disables filtering, allowing the player to
# include every category or every difficulty.
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

# Extention: file I/O saves the player's best accuracy between program runs.
# Using the script's folder keeps the save file in a predictable location.
HIGH_SCORE_FILE: Path = Path(__file__).with_name("trivia_high_score.txt")

# Reusable function handles both menus, so input validation only needs to be written once
def choose_from_menu(title: str, options: list[str]) -> str: # Display a numbered menu and return the option selected by the player.
    print(title)

    # enumerate gives each option a number starting at 1.
    for position, option in enumerate(options, start=1):
        print(f"    {position}) {option}") # Display the current option with its corresponding menu number.

    # Convert input to an integer inside try/except so letters and other
    # invalid input cause another prompt instead of crashing the program.
    while True:
        choice: str = input("Your choice number): ").strip()

        try: # Forces player to enter a valid letter.
            selected_number: int = int(choice)
        except ValueError:
            print("Please enter a whole-number menu choice.")
            continue

        if 1 <= selected_number <= len(options): # Checks both ends of the valid range.
            return options[selected_number -1]

        print(f"Please enter a number from 1 to {len(options)}")

# This function reads the best saved score.
def load_best_accuracy(filename: Path) -> float:
    # Load the saved best accuracy, or return zero if no valid record exists.
    try:
        with filename.open("r", encoding="utf-8") as score_file:
            saved_value: str = score_file.read().strip()

        saved_accuracy: float = float(saved_value)
        if 0.0 <= saved_accuracy <= 100.0:
            return saved_accuracy

        # Ignore invalid values rather than letting a damage save affect play.
        return 0.0
    except FileNotFoundError:
        # A missing file simply means the player has not set a saved record yet.
        return 0.0
    except (OSError, ValueError):
        print("The saved record could not be read; starting without a saved record.")
        return 0.0

# This function writes a new personal best percentage and returns 
def save_best_accuracy(filename: Path, accuracy: float) -> bool:
    # Save a new best accuracy and report whether the save succeeded.
    try:
        with filename.open("w", encoding="utf-8") as score_file:
            score_file.write(f"{accuracy:.2f}")
        return True
    except OSError:
        #The game should remain playable even if the folder is read-only.
        return False


play_again: str = "Y"

while play_again == "Y":

    print("+-----------------------------------------------------------------+")
    print("|                    Welcome to the Trivia Game!                  |")
    print("| Answer each question by typing the letter of your choice.       |")
    print("+-----------------------------------------------------------------+")
    print()

    category: str = choose_from_menu("Choose a category:", category_options)
    print()
    difficulty: str = choose_from_menu("Choose a difficulty", difficulty_options)
    print()

    # Keep only the questions that match the selected category and difficulty.
    question_pool: list[dict[str, str | list[str]]] = []

    for question in questions:
        question_category = cast(str, question["category"])
        question_difficulty = cast(str, question["difficulty"])

        category_matches: bool = (
            category == "All Categories" or question_category == category
        )
        difficulty_matches: bool = (
            difficulty == "All difficulties"
            or question_difficulty == difficulty
        )

        if category_matches and difficulty_matches:
            question_pool.append(question)

    # Save the total before popping questions from the pool during the round.
    total_questions: int = len(question_pool)

    # Safety net in case a category/difficulty combination has no questions.
    if total_questions == 0:
        print(
            "Sorry, there are no questions for that category and difficulty."
            "Please choose again."
        )
        print()
        continue

    print(f"Starting a game with {total_questions} question(s). Good luck!")
    print()

    score: int = 0  # score  -> counts how many questions the player has gotten right so far.
    question_number: int = 0  # question_number  -> tracks which question in the "questions" list we're currently on.

    # Removing each random question prevents it from appearing twice in a round.
    while len(question_pool) > 0:
        random_position: int = random.randint(0, len(question_pool) - 1)
        current_question: dict[str, str | list[str]] = question_pool.pop(random_position)

        current_category: str = cast(str, current_question["category"])
        current_difficulty: str = cast(str, current_question["difficulty"])
        question_text: str = cast(str, current_question["question"])
        choices: list[str] = cast(list[str], current_question["choices"])
        correct_answer: str = cast(str, current_question["answer"])

        print(
            f"Question {question_number + 1}"
            f"[{current_category} - {current_difficulty}]: {question_text}"
        )

        for choice in choices:
            print(choice)

        valid_letters: list[str] = [choice[0] for choice in choices]
        answer: str = input("Your answer (just the letter): ").strip().upper()

        while answer not in valid_letters: # Keep re-asking until they actually type one of the real choices.
            print(
                f"'{answer}' isn't one of the choices. "
                f"Please enter one of: {', '.join(valid_letters)}"
            )
            answer = input("Your answer (just the letter): ").strip().upper()

        if answer == correct_answer: # If the player's answer matches the correct answer for this question, they got it right.
            print("Correct!")
            score += 1
        else:
            print(f"Sorry that's incorrect, the correct answer was {correct_answer}.")

        print()
        question_number += 1

    print("+-----------------------------------------------------------------+")
    print(f"You scored {score} out of {total_questions}!") # Displays the final score.

    if score == 0:
        print(
            "When your parents dropped you off at the bus stop, "
            "did you even get on?"
        )

    elif score == total_questions:
        print("You got the perfect score!")

    else:
        print("You could've done better, but at least you did better than zero.")

    # Accuracy makes results comparable between short filtered rounds and full games.
    current_accuracy: float = (score / total_questions) * 100.0
    previous_best: float = load_best_accuracy(HIGH_SCORE_FILE)

    print(f"This round's accuracy: {current_accuracy:.1f}%")

    if current_accuracy > previous_best:
        if save_best_accuracy(HIGH_SCORE_FILE, current_accuracy):
            print(f"New personal best saved: {current_accuracy:.1f}%!")
        else:
            print(
                "you achieved a new personal best, but the record could not be saved."
            )
    else:
        print(f"Personal best accuracy: {previous_best:.1f}%")

    print("+-----------------------------------------------------------------+")
    print()

    play_again = input("Do you want to play again? (Y/N): ").strip().upper() # Ask the player if they want another round. Anything other than "Y" ends the outer loop.
    print()

print("Thanks for playing!")
