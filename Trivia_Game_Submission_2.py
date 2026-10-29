"""
Trivia_Game Submission 2.py
Roland, Gabby, Abir

A multiple-choice trivia game. The player picks a category and difficulty,
is shown the matching questions in a random order, types the letter of their
answer to each one, and the game keeps track of how many they got right.
"""

import random   # Allows .randint importation. Gives the ability of for the questions to be randomized.
from datetime import datetime   # Gives datetime.now() so each saved score can be stamped with the date and time it was set.
from pathlib import Path    # Most efficient method for creating files on the user's computer.
from typing import cast     # Importing cast tells Pylance a dictionary value's expected type e.g. str or list[str]

"""This is the full set of trivia questions. It's a LIST of DICTIONARIES: each
item in the list is one question, and each question is a dictionary
that bundles together everything that question needs."""

questions: list[dict[str, str | list[str]]] = [
    # ---------------------------- Geography ----------------------------
    {
        "question": "What is the capital of France?",   # "question" -> the text shown to the player.
        "choices": [    # "choices" -> the list of choices shown to the player.
            "A) Berlin",
            "B) Madrid",
            "C) Paris",
            "D) Rome",
        ],
        "answer": "C",  # "answer" -> the correct answer.
        "category": "Geography",    # "category" -> the topic the question belongs to.
        "difficulty": "Easy",   # "difficult" -> "Easy", "Medium" or "Hard"
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
            "C) Canberra",
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
            "B) Lake Victoria",
            "C) Lake Tanganyika",
            "D) Lake Baikal",
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
            "D) Argon",
        ],
        "answer": "B",
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
            "C) Mitochondria",
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
            "B) Universal Serial Bus",
            "C) Unified Software Backup",
            "D) Universal Storage Block",
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

# The final option in each menu disables filtering, allowing the player to include every category or every difficulty.
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
HIGH_SCORE_FILE: Path = Path(__file__).with_name("Your Trivia High Score.txt")

# Both the category and difficulty menus use this function to display options.
def choose_from_menu(title: str, options: list[str]) -> str:    # Display a numbered menu and return the option selected by the player.
    print(title)

    # enumerate gives each option a number starting at 1.
    for position, option in enumerate(options, start = 1):
        print(f"    {position}) {option}")  # Display the current option with its corresponding menu number.

    # Convert the user's input to an integer inside try/except so letters and other invalid input cause another prompt instead of crashing the program.
    while True:
        choice: str = input("Your choice number: ").strip()

        try:    # Forces player to enter a number.
            selected_number: int = int(choice)

        except ValueError:
            print("Please enter a whole-number menu choice.")
            continue

        if 1 <= selected_number <= len(options):    # Checks both ends of the valid range.
            return options[selected_number - 1]

        print(f"Please enter a number from 1 to {len(options)}")

# This function reads the best saved score.
def load_best_accuracy(filename: Path, category: str, difficulty: str) -> float:
    best_accuracy: float = 0.0

    try:    # Load the saved best accuracy, or return zero if no valid record exists.
        with filename.open("r", encoding = "utf-8") as score_file:  # Opens the high-score file for reading and close it when finished.
            for line in score_file:
                # Split the saved record into its separate fields.
                parts: list[str] = line.split("|", maxsplit = 3)

                # Ignore records that do not contain all required fields.
                if len(parts) < 4:
                    continue

                # Extract the saved category and difficulty.
                saved_category: str = parts[1].partition(":")[2].strip()
                saved_difficulty: str = parts[2].partition(":")[2].strip()

                # Only compare scores from the same category and difficulty.
                if (
                    saved_category != category
                    or saved_difficulty != difficulty
                ):
                    continue

                # Extracts the percentage from the beginning of the record.
                number_text: str = parts[0].replace("%", "").strip()

                try:
                    saved_accuracy: float = float(number_text)

                except ValueError:
                    continue

                # Keeps the highest valid accuracy for this selection.
                if 0.0 <= saved_accuracy <= 100.0 and saved_accuracy > best_accuracy:
                    best_accuracy = saved_accuracy

    except FileNotFoundError:
        return 0.0  # A missing file simply means the player has not set a saved record yet.

    except OSError:   # Handles file errors without crashing the game.
        print("The saved record could not be read; starting without a saved record.")
        return 0.0

    return best_accuracy

# Writes a new personal best percentage and returns 
def save_best_accuracy(filename: Path, accuracy: float, category: str, difficulty: str) -> bool:
    timestamp: str = datetime.now().strftime("%m/%d/%Y %I:%M %p")

    # Save a new best accuracy and report whether the save succeeded.
    try:
        # Add a newline only when a non-empty score file already exists.
        separator: str = ""
        if filename.exists() and filename.stat().st_size > 0:
            separator = "\n"

        # Append the new record instead of overwriting previously saved scores.
        with filename.open("a", encoding = "utf-8") as score_file:
            score_file.write(
                f"{separator}{accuracy:.2f}% | Category: {category}"
                f" | Difficulty: {difficulty} | {timestamp}"
            )
        return True

    except OSError:
        return False    # The lets the game remain playable even if the file is read-only.

# Function for deleting all of the user's saved scores.
def reset_high_scores(filename: Path) -> None:
    # If the user doesn't have a file to delete, it will tell them so.
    if not filename.exists():
        print("There are no saved high scores to delete.")
        return

    confirm: str = input("Delete ALL saved high scores? This can't be undone. (Y/N): ").strip().upper()

    if confirm != "Y":
        print("Nothing was deleted.")
        return

    try:
        # Clear saved scores while keeping the file available for future records.
        filename.unlink()
        print("All saved high scores have been deleted.")
    # Prevents the game from crashing.
    except OSError:
        print("The saved high scores could not be deleted.")


play_again_prompt: str = ("Do you want to play again? (Y/N, or D to delete all saved high scores): ")

play_again: str = "Y"

print("+-----------------------------------------------------------------+")
print("|                    Welcome to the Trivia Game!                  |")
print("|    Answer each question by typing the letter of your choice.    |")
print("+-----------------------------------------------------------------+")
print()

while play_again == "Y":

    # Ask for a category and store the user's selection.
    category: str = choose_from_menu("Choose a category:", category_options)
    print()

    # Use the same menu function for difficulty.
    difficulty: str = choose_from_menu("Choose a difficulty:", difficulty_options)
    print()

    # Keep only the questions that match the selected category and difficulty.
    question_pool: list[dict[str, str | list[str]]] = []

    # Checks every question in the master list to decide whether it matches the two filters.
    for question in questions:
        question_category = cast(str, question["category"])
        question_difficulty = cast(str, question["difficulty"])

        # A question matches the category if the player selected all categories or this question has the chosen category.
        category_matches: bool = (
            category == "All Categories" or question_category == category
        )
        # Applies the same rule to difficulty.
        difficulty_matches: bool = (
            difficulty == "All difficulties"
            or question_difficulty == difficulty
        )

        if category_matches and difficulty_matches:
            question_pool.append(question)  # Add matching questions to the round-specific pool.

    # Save the total before popping questions from the pool during the round.
    total_questions: int = len(question_pool)

    # Failsafe against an empty selection, which would otherwise leave the game with no questions to ask.
    if total_questions == 0:
        print(
            "Sorry, there are no questions for that category and difficulty."
            "Please choose again."
        )
        print()
        continue

    print(f"Starting a game with {total_questions} questions. Good luck!")
    print()

    score: int = 0  # score  -> Start each round with zero correct answers.
    question_number: int = 0  # question_number  -> Track how many questions have been asked so the displayed question number can increase.

    # Removing each random question prevents it from appearing twice in a round.
    while len(question_pool) > 0:
        random_position: int = random.randint(0, len(question_pool) - 1)    # Chooses a random question.
        current_question: dict[str, str | list[str]] = question_pool.pop(random_position)   # pop both retrieves the selected question and removes it

        current_category: str = cast(str, current_question["category"]) # Reads the category
        current_difficulty: str = cast(str, current_question["difficulty"]) # Reads the difficulty
        question_text: str = cast(str, current_question["question"]) # Gets the question text separately so the print statement is still readable.
        choices: list[str] = cast(list[str], current_question["choices"]) # Communicates to pylance the choice value is expected to be a list of string.
        correct_answer: str = cast(str, current_question["answer"]) # Keep the correct answer letter separate from the choices shown to the player. 

        print(
            f"Question {question_number + 1}"
            f" [{current_category} - {current_difficulty}]: {question_text}"
        )

        # Loop the current question's choices so each option is printed on its own line.
        for choice in choices:
            print(choice)

        # Read allowed letters from the choices so validation matches each question.
        valid_letters: list[str] = [choice[0] for choice in choices]
        answer: str = input("Your answer (just the letter): ").strip().upper()

        while answer not in valid_letters:  # Keep re-asking until they actually type one of the real choices.
            print(
                f"'{answer}' isn't one of the choices. "
                f"Please enter one of: {', '.join(valid_letters)}"
            )
            answer = input("Your answer (just the letter): ").strip().upper()

        if answer == correct_answer:    # Checks if the user inputed the correct answer.
            print("Correct!")
            score += 1
        else:
            print(f"Sorry that's incorrect, the correct answer was {correct_answer}.")

        print()
        question_number += 1

    print("+-----------------------------------------------------------------+")
    print(f"You scored {score} out of {total_questions}!")  # Displays the final score.

    if score == 0:
        print("When your parents dropped you off at the bus stop, did you even get on?")

    elif score == total_questions:
        print("You got the perfect score!")

    else:
        print("You could've done better, but at least you did better than zero.")

    current_accuracy: float = (score / total_questions) * 100.0 # Converts the score to a percentage.
    previous_best: float = load_best_accuracy(HIGH_SCORE_FILE, category, difficulty)  # Loads the previous best from disk.

    print(f"This round's accuracy: {current_accuracy:.1f}%")

    # Only replaces the saved record if the current round beats the previous best.
    if current_accuracy > previous_best:
        if save_best_accuracy(HIGH_SCORE_FILE, current_accuracy, category, difficulty):
            print(f"New personal best saved: {current_accuracy:.1f}%!")
            print('Your high score has been added to "Your Trivia High Score.txt"')
        else:
            print(
                "you achieved a new personal best, but the record could not be saved."
            )
    else:
        print(f"Personal best accuracy: {previous_best:.1f}%")

    print("+-----------------------------------------------------------------+")
    print()

    # Ask the player if they want another round. Anything other than "Y" or "y" ends the outer loop.
    # Typing "D" deletes every saved high score (after a confirmation) and then asks the question again.
    play_again = input(play_again_prompt).strip().upper()

    while play_again == "D":
        reset_high_scores(HIGH_SCORE_FILE)
        print()
        play_again = input(play_again_prompt).strip().upper()

    print()

print("Thanks for playing!")
