# Hangman Game

import random

# Step 1: Word list
words = ["python", "programming", "hangman", "shadowfox", "developer", "internship"]

# Step 2: Choose a random word
chosen_word = random.choice(words)
word_length = len(chosen_word)

# Step 3: Game setup
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman! ")
print("_ " * word_length)  # Show blanks for the word

# Step 4: Game loop
while wrong_guesses < max_attempts:
    guess = input("\nGuess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is in word
    if guess in chosen_word:
        print(" Good guess!")
    else:
        print(" Wrong guess!")
        wrong_guesses += 1

    # Show current progress
    display_word = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("\n Congratulations! You guessed the word:", chosen_word)
        break

# If lost
if wrong_guesses == max_attempts:
    print("\n Game Over! The word was:", chosen_word)
