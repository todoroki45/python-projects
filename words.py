import random

# List of words to guess from
words = ["apple", "banana", "cherry", "orange", "lemon", "pear", "grape", "watermelon"]

# Select a random word from the list
word = random.choice(words)

# Create a list of underscores for each letter in the word
word_guess = ["_"] * len(word)

# Set the initial number of guesses to 0
num_guesses = 0

# Loop until the player runs out of guesses or guesses the word
while num_guesses < 6 and "_" in word_guess:
    # Print the current state of the word
    print(" ".join(word_guess))

    # Ask the player to guess a letter
    print("LETTERS :-D [apple, banana, cherry, orange, lemon, pear, grape, watermelon]")
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in word_guess:
        print("You've already guessed that letter. Try again.")
        continue

    # Check if the letter is in the word
    if guess in word:
        # Update the word_guess list with the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                word_guess[i] = guess
    else:
        # Increment the number of guesses
        num_guesses += 1
        print("Wrong! You have", 6 - num_guesses, "guesses left.")

# Print the final state of the word
print(" ".join(word_guess))

# Check if the player won or lost
if "_" not in word_guess:
    print("Congratulations, you guessed the word!")
else:
    print("Sorry, you ran out of guesses. The word was", word + ".")
