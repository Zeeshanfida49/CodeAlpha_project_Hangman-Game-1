import random

# List of predefined words
words = ["apple", "brain", "cloud", "plant", "stone"]

# Randomly choose a word from the list
word_to_guess = random.choice(words)
guessed_letters = []  # Letters guessed by the player
tries_left = 6  # Maximum incorrect guesses
display_word = ["_"] * len(word_to_guess)  # Hidden word with underscores

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 chances to guess incorrectly.\n")

# Main game loop
while tries_left > 0 and "_" in display_word:
    print("Word:", " ".join(display_word))
    print(f"Tries left: {tries_left}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good job! Letter found.\n")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
    else:
        print("Oops! Wrong guess.\n")
        tries_left -= 1

# Game over messages
if "_" not in display_word:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("Sorry, you ran out of tries. The word was:", word_to_guess)

