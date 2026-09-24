"""
    trivia_game.py
    Roland, Gabby, Abir

    A multiple-choice trivia game. The player is shown a question and a set
    of lettered choices, types the letter of their answer, and the game
    keeps track of how many they got right.
"""

# This is the full set of trivia questions. It's a LIST of DICTIONARIES: each
# item in the list is one question, and each question is a dictionary that
# bundles together everything that question needs.

questions: list[dict[str, str | list[str]]] = [ 
    {
        "question": "What is the capital of France?",   # "question" -> the text shown to the player
        "choices": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],   # "choices" -> the list of choices shown to the player
        "answer": "C",  # "answer" -> the correct answer
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B",
    },
    {
        "question": "How many continents are there?",
        "choices": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "C",
    },
    {
        "question": "What does CPU stand for?",
        "choices": ["A) Central Processing Unit", "B) Computer Personal Unit", "C) Central Program Utility", "D) Core Processing Unit"],
        "answer": "A",
    }
]

play_again: str = "Y"

while play_again == "Y":

    print("+-----------------------------------------------------------------+")
    print("|                    Welcome to the Trivia Game!                  |")
    print("| Answer each question by typing the letter of your choice.       |")
    print("+-----------------------------------------------------------------+")
    print()

    score: int = 0  # score  -> counts how many questions the player has gotten right so far.
    index: int = 0  # index  -> tracks which question in the "questions" list we're currently on.

    while index < len(questions):   # Outer loop: runs once per question. It keeps going as long as there are still questions left to ask
        current_question = questions[index]     # Pull out the single dictionary for whichever question the player is on right now, giving easy access to the "question", "choices", and "answer" values.

        print(f"Question {index + 1}: {current_question['question']}")  # Show the question text. index + 1 is just for display, so the player

        choice_index = 0
        while choice_index < len(current_question["choices"]):  # Inner loop: runs once per choice for the current question. It keeps going as long as there are choices left to show.
            print(current_question["choices"][choice_index])    # Show the choice text. The choices are already lettered, so we don't need to add letters here.
            choice_index += 1   # Increment the choice_index so we can move on to the next choice in the next iteration of this inner loop.

        answer = input("Your answer (just the letter): ").strip().upper()   # Get the player's answer, remove any extra whitespace, and convert it to uppercase so it can be compared to the correct answer.

        if answer == current_question["answer"]:    # If the player's answer matches the correct answer for this question, they got it right
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer was {current_question['answer']}.")

        print()
        index += 1

    print("+-----------------------------------------------------------------+")
    print(f"You scored {score} out of {len(questions)}!") # Displays the final score

    if score == 0:
        print("When your parents dropped you off at the bus stop, did you even get on?")

    if score == len(questions):
        print("You got the perfect score!")
    
    elif score > 0 & score < len(questions):
        print("You could've done better, but at least you did better than zero.")

    print("+-----------------------------------------------------------------+")
    print()

    play_again = input("Do you want to play again? (Y/N): ").strip().upper()   # Ask the player if they want another round. Anything other than "Y" ends the outer loop.
    print()

print("Thanks for playing!")
