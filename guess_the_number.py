import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to 'Guess the Number'!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")

    # Game loop
    while not guessed:
        # Increment the number of attempts
        attempts += 1

        # Get the user's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check the user's guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

# Start the game
if __name__ == "__main__":
    guess_the_number()
