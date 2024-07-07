# Python_Word_Sleuth: A Guessing Words Game

import random

user_guess_wordbook = {
    "python": "A programming language.",
    "computer": "An electronic device for data processing.",
    "keyboard": "Input keys arranged for computer operation.",
    "vim": "A configurable text editor.",
    "D&D": "Tabletop role-playing game.",
    "chess": "Strategic board game.",
    "scrabble": "Word game with tiles.",
    "monopoly": "Property trading board game.",
    "tetris": "Tile-matching puzzle game.",
    "jupiter": "Fifth planet from the sun and the largest in the solar system.",
    "clash of clans": "Mobile strategy video game.",
    "Star Wars": "Epic space opera franchise.",
    "Hogwarts Legacy": "Game based on Harry Potter.",
    "black hole": "Region of spacetime with strong gravity.",
    "spaceship": "Vehicle for space travel.",
    "SpaceX": "Space transportation company.",
    "NASA": "United States space agency.",
    "interstellar": "Related to space travel beyond the solar system.",
    "saturn": "Sixth planet from the sun, with beautiful rings.",
}


def pick_random_word():
    return random.choice(list(user_guess_wordbook.keys()))


def hint_provider(word):
    return user_guess_wordbook[word]


def execute_word_sleuth():
    word_guesser = pick_random_word()
    word_hint = hint_provider(word_guesser)
    allowed_user_attempts = 7

    try:
        while allowed_user_attempts > 0:
            print(f"Hint for the word you're guessing: {word_hint}")
            print(f"Remaining allowed attempts: .... {allowed_user_attempts}")
            user_guessed_input = input("Please type your guess here:")
            if user_guessed_input.lower() == word_guesser.lower():
                print("Correct guess!")
                break  # Exits the loops if the user's guess is correct
            elif user_guessed_input.isnumeric():
                print("Invalid Input, please input a string input and then proceed")
                allowed_user_attempts -= 1
            elif not user_guessed_input.isalpha():
                print("Invalid Input, please input a string input and then proceed")
                allowed_user_attempts -= 1
            else:
                print("Incorrect guess. Please guess again.")
                allowed_user_attempts -= 1

        # Responsible for checking if the player has ran out of attempts or not:
        if allowed_user_attempts == 0:
            print(f"== Sorry, you've ran out of attempts ==\nThe word you were guessing for was:", word_guesser)
    except KeyboardInterrupt:
        print("\nGame interrupted...stopping execution of the game!")


if __name__ == '__main__':
    randomly_picked_word = pick_random_word()
    print(f"A random word for the user: {randomly_picked_word}")
    execute_word_sleuth()
