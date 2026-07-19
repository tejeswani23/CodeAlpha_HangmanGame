import random

words = ["code", "alpha", "intern", "ship", "program"]

secret_word = random.choice(words)
guessed_letters = []
attempts = 6

print(" #HANGMAN GAME# ")

while attempts > 0:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Remaining Attempts:", attempts)

    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", secret_word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Right Guess!")
    else:
        attempts -= 1
        print("Wrong Guess!")

if attempts == 0:
    print("\nGame Over!!!")
    print("The correct word was:", secret_word)