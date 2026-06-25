# Hangman: Implement the word-guessing game with visual progress and hints.
# The script chooses a secret word and lets the player guess letters one by one.

import random


def hangman(word):
    # Convert the secret word to lowercase so guesses are case-insensitive.
    word = word.lower()

    # Track which letters have already been guessed by the player.
    guessed_letters = []

    # Number of wrong guesses the player is allowed before losing.
    attempts = 6

    # Build the display word using underscores for each hidden letter.
    display_word = ['_' for _ in word]

    print("Welcome to Hangman!")
    print("You have", attempts, "attempts to guess the word.")
    
    # Loop until the player either guesses the word or runs out of attempts.
    while attempts > 0 and '_' in display_word:
        # Show current progress and letters guessed so far.
        print("\nCurrent word:", ' '.join(display_word))
        print("Guessed letters:", ', '.join(guessed_letters) or 'None')

        # Ask the player for a single letter guess.
        guess = input("Guess a letter: ").lower()

        # Validate the input to ensure only one alphabet character is entered.
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Avoid repeated guesses for the same letter.
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Store the new guessed letter.
        guessed_letters.append(guess)

        # If the guessed letter is in the secret word, reveal it.
        if guess in word:
            print("Good guess!")
            for index, letter in enumerate(word):
                if letter == guess:
                    display_word[index] = guess
        else:
            # Deduct one attempt for a wrong guess.
            attempts -= 1
            print("Wrong guess! You have", attempts, "attempts left.")

    # After the loop, check whether the player has won or lost.
    if '_' not in display_word:
        print("\nCongratulations! You've guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)


def main():
    # A small list of sample words to choose from for the game.
    # You can add more words here to make the game more interesting.
    word_list = [
        "python",
        "hangman",
        "development",
        "challenge",
        "internet",
    ]

    # Select a random word from the list as the secret word.
    secret_word = random.choice(word_list)

    # Start the Hangman game using the selected word.
    hangman(secret_word)


# Only run the game when this file is executed directly.
if __name__ == "__main__":
    main()