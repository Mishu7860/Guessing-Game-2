import random

def number_guessing_game():
    # Get the range from the user
    print("Welcome to the Number Guessing Game!")
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    # Generate a random number within the specified range
    secret_number = random.randint(lower_bound, upper_bound)
    
    print(f"\nI have generated a random number between {lower_bound} and {upper_bound}.")
    print("Try to guess it!")

    # Initialize the variable for storing the user's guess
    guess = None
    
    # Loop until the user guesses the correct number
    while guess != secret_number:
        try:
            # Get user input and convert it to an integer
            guess = int(input(f"Enter your guess ({lower_bound} to {upper_bound}): "))
            
            # Provide feedback to the user
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number}.")
        except ValueError:
            print("Please enter a valid integer.")
        
# Example usage:
number_guessing_game()
