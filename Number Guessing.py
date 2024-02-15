# Import the random module
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize variables
guess = 0
attempts = 0

# Create a loop for the game
while guess != secret_number:
    # Get user input for their guess
    guess = int(input("Guess the number between 1 and 100: "))

    # Increment the attempts
    attempts += 1

    # Check if the guess is correct
    if guess == secret_number:
        print(f"Congratulation! You guessed the correct number {secret_number} in {attempts} attempts.")
    else:
        # Provide hints for higher or lower guesses
        if guess < secret_number:
            print("Try again! Guess higher")
        else:
            print("Try again! Guess lower")