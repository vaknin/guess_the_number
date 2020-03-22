# Imports
import random, os

# Globals
global maxNum, guesses, guess
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

# Welcome message
clear()
input("Welcome to 'Guess The Number'!\nYou will be asked to guess which number was randomly chosen.")
clear()

# Game Loop
while True:

    # Retrieve the maximum number
    while True:
        try:
            maxNum = int(input("Please enter the highest number possible: "))
            break
        except ValueError:
            print("not a valid integer")

    clear()

    # Retrieve the number of guesses
    while True:
        try:
            guesses = int(input("Please enter the number of guesses you would like to have: "))
            break
        except ValueError:
            print("not a valid integer")

    # Generate the random number
    randomNumber = random.randrange(1, maxNum + 1)
    clear()

    # Announce the game has started and explain rules
    print(f"The number has been selected, please choose a number between 1 and {maxNum}.")

    # Check for remaining guesses
    while guesses > 0:

        # Retrieve the user's guess
        while True:
            try:
                guess = int(input("Make a guess: "))
                break
            except ValueError:
                print("not a valid guess!")

        # Clear screen
        clear()

        # Guess was correct
        if guess == randomNumber:
            print("Good Job! You've guessed the number!")
            break

        # Guess too high
        elif guess > randomNumber:
            print(f"{guess} is too high!")

        # Guess too low
        elif guess < randomNumber:
            print(f"{guess} is too low!")

        # Decrease number of guesses by 1
        guesses = guesses - 1

    # Game over
    if guesses == 0:
        clear()
        print(f"Game over!\nThe number was {randomNumber}, better luck next time!")

    # Play again?
    choice = input("Would you like to play again? (Y/N)\n")
    clear()
    if choice != "Y" and choice != "y":
        break