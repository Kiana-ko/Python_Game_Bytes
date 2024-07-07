import random

Hangman_wordList_for_user = ["Wormhole", "Black hole", "spaceship", "Comet", "steroid", "White hole", "Cosmic dust"]


def hangman_hint_giver(word, guessed_letters):
    hint_word = ""
    for char in word:
        if char != ' ':
            if char.upper() in guessed_letters:
                hint_word += char + ' '
            else:
                hint_word += "_ "
        else:
            hint_word += "  "  
    return hint_word


def hangman_game_restart():
    user_restart_option = input("Do you want to replay the Hangman game? (yes/no): ").lower()
    if user_restart_option == "yes":
        play_hangman_game()  
    else:
        print("Thanks for playing!")


def play_hangman_game():
    selected_word = random.choice(Hangman_wordList_for_user).upper()
    revealed_word = list(selected_word)
    guessed_letters = []

    print("Welcome to Hangman game!\nPlease guess a word to begin:")

    
    hint_word = hangman_hint_giver(selected_word, guessed_letters)
    print("Word to guess:", hint_word)

    allowed_user_attempts = 10
    while "_" in hint_word and allowed_user_attempts > 0:
        user_guess = input("Please enter a letter or the whole word: ").upper()

        if user_guess.isalpha():
            if len(user_guess) == 1:
                if user_guess in selected_word:
                    guessed_letters.append(user_guess)
                    hint_word = hangman_hint_giver(selected_word, guessed_letters)
                    print("Word to guess:", hint_word)
                else:
                    allowed_user_attempts -= 1
                    print('Incorrect guess. You have', allowed_user_attempts, 'more attempts.')
            else:
                # Split the user's guess into individual words
                user_guess_words = user_guess.split()
                # Check if the guess matches the selected word
                if user_guess.upper() == selected_word:
                    hint_word = selected_word
                    print("Congratulations! You guessed the word correctly:", selected_word)
                    break
                # Check if all words in the guess match parts of the selected word
                elif any(letter.upper() in selected_word for letter in user_guess):
                    # Update guessed letters for each letter in the guess
                    for letter in user_guess:
                        if letter.upper() not in guessed_letters:
                            guessed_letters.append(letter.upper())
                    hint_word = hangman_hint_giver(selected_word, guessed_letters)
                    print("Word to guess:", hint_word)
        else:
            if user_guess.upper() == selected_word:
                hint_word = selected_word
                print("Congratulations! You guessed the word correctly:", selected_word)
                break
            elif user_guess.upper() in Hangman_wordList_for_user:
                guessed_letters |= set(user_guess.upper())
                hint_word = hangman_hint_giver(selected_word, guessed_letters)
                print("Word to guess:", hint_word)
            else:
                print("Incorrect guess. Try again.")

    if "_" in hint_word:
        print('Sorry, you lost. The word was:', selected_word)

    hangman_game_restart()  


if __name__ == '__main__':
    play_hangman_game()  
