# This is a rough template for how the paths will work.

def get_choice(prompt: str, options: tuple[str, ...]) -> str: # Defines a function that asks the player for a choice. Options is a tuple containing the different choices.
    while True:
        choice = input(prompt).strip().upper()
        if choice in options:
            return choice
        print(f"Choose one of: {', '.join(options)}")

def main() -> None:
    play_again: str = "Y"
    while play_again == "Y":

        print("START")
        choice = get_choice("Choose Path A or Path B: ", ("A", "B"))

        if choice == "A":
            print("PATH A")
            choice = get_choice("Choose Path A1 or Path A2: ", ("A1", "A2"))

            if choice == "A1":
                print("PATH A1")
                choice = get_choice("Choose Yes or NO: ", ("YES", "NO"))


                if choice == "YES":
                    print("PATH A1A")
                    print("ENDING A1A")
                else:
                    print("PATH A1B")
                    print("ENDING A1B")

            else:
                print("PATH A2")
                print("ENDING A2")

        else:
            print("PATH B")
            choice = get_choice("Choose YES or NO: ", ("YES", "NO"))

            if choice == "YES":
                print("PATH B1")
                print("ENDING B1")
            else:
                print("PATH B2")
                print("ENDING B2")
    play_again = input("Do you want to play again? (Y/N): ").strip().upper()   # Ask the player if they want another round. Anything other than "Y" ends the outer loop.


if __name__ == "__main__":
    main()
