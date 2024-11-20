import random  # Importing the random module to generate random numbers

# Function to get valid integer input from the user within a specific range
def get_integer_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))  # Get user input and convert to integer
            if min_value <= value <= max_value:  # Validate range
                return value  # Return valid input
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Function to display a goodbye message when the player chooses to quit
def display_goodbye_message():
    print("\n" + "=" * 40)
    print("Thank you for playing! Goodbye!")
    print("=" * 40)

# Main game function that controls the flow of the guessing game
def guessing_game():
    score = 0  # Player's score
    streak = 0  # Winning streak counter
    max_range = 100  # Initial number range
    max_attempts = 10  # Initial number of attempts
    is_first_game = True  # Flag to track if this is the first round

    while True:  # Infinite loop for the game
        if is_first_game:
            print("\n" + "?" * 40)
            print("WELCOME TO THE GUESSING GAME!")
            print("?" * 40)
            is_first_game = False  # Set flag to False after the first round

        # Ask the player to select a difficulty level
        print("Select Difficulty Level:")
        print("1. Easy (1-100, 10 attempts)")
        print("2. Medium (1-200, 7 attempts)")
        print("3. Hard (1-300, 5 attempts)")
        difficulty = get_integer_input("Enter your choice (1/2/3): ", 1, 3)

        # Set the number range and attempts based on the difficulty
        if difficulty == 1:
            max_range = 100
            max_attempts = 10
        elif difficulty == 2:
            max_range = 200
            max_attempts = 7
        else:
            max_range = 300
            max_attempts = 5

        # Generate the number to guess
        number_to_guess = random.randint(1, max_range)
        attempts = 0  # Initialize attempt counter

        # Display information about the game
        print(f"\nI've chosen a number between 1 and {max_range}.")
        print(f"You have {max_attempts} attempts. Let's begin!")

        # Main guessing loop
        while attempts < max_attempts:
            guess = get_integer_input(f"Enter your guess (1-{max_range}): ", 1, max_range)
            attempts += 1  # Increment attempt count

            if guess < number_to_guess:
                proximity_hint = abs(number_to_guess - guess)
                if proximity_hint <= max_range * 0.1:  # Within 10% of the number
                    print(f"You're very close! But it's low, You have {max_attempts - attempts} attempts left.")
                else:
                    print(f"Too low! {max_attempts - attempts} attempts left.")
            elif guess > number_to_guess:
                proximity_hint = abs(guess - number_to_guess)
                if proximity_hint <= max_range * 0.1:  # Within 10% of the number
                    print(f"You're very close! But it's high, You have {max_attempts - attempts} attempts left.")
                else:
                    print(f"Too high! {max_attempts - attempts} attempts left.")
            else:
                streak += 1  # Increment winning streak
                score += (max_attempts - attempts + 1) * 10  # Calculate score
                print(f"\n🎉 That's correct! You guessed the number in {attempts} attempts! 🎉")
                print(f"Your current score is: {score}!")
                print(f"You have a winning streak of: {streak} 🎯")
                break  # Exit guessing loop if correct

        # If the player runs out of attempts without guessing
        if attempts == max_attempts and guess != number_to_guess:
            streak = 0  # Reset streak on loss
            print(f"\nSorry, you've used all your attempts. The number was {number_to_guess}.")
            print(f"Your final score is: {score}")

        # Ask the player if they want to play again
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()

        # Adaptive Difficulty: Adjust based on performance
        if play_again == "yes":
            if attempts < max_attempts // 2:  # Player guessed quickly
                max_range = min(1000, max_range + 50)  # Increase range, cap at 1000
                max_attempts = max(3, max_attempts - 1)  # Decrease attempts, min cap at 3
                print("\nYou performed well! Difficulty increased:")
                print(f"- Range increased to {max_range}")
                print(f"- Attempts reduced to {max_attempts}")
            elif attempts == max_attempts:  # Player used all attempts
                max_range = max(50, max_range - 50)  # Decrease range, min cap at 50
                max_attempts += 1  # Increase attempts
                print("\nYou struggled last round. Difficulty adjusted:")
                print(f"- Range reduced to {max_range}")
                print(f"- Attempts increased to {max_attempts}")
        else:
            display_goodbye_message()  # Show goodbye message
            break  # Exit game loop

# Start the game if this script is run directly
if __name__ == "__main__":
    guessing_game()
