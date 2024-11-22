import random  # Importing the random module to generate random numbers for the guessing game
import os  # Importing os module to clear the screen based on the operating system

# Function to get valid integer input from the user within a specific range
def get_integer_input(prompt, min_value, max_value):
    while True:  # Loop until valid input is entered
        try:
            value = int(input(prompt))  # Prompt the user for input and convert it to an integer
            if min_value <= value <= max_value:  # Check if the input is within the specified range
                return value  # If the input is valid, return the value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")  # If out of range, ask again
        except ValueError:
            print("Invalid input. Please enter a valid integer.")  # If input isn't an integer, ask again

# Function to display a goodbye message when the player chooses to quit
def display_goodbye_message():
    print("\n" + "=" * 40)  # Print separator line
    print("Thank you for playing the Guessing Game! See ya next time!")  # Display goodbye message
    print("=" * 40)  # Print another separator line

# Function to save the high score to a file
def save_high_score(cumulative_score):
    try:
        # Try opening the high_score.txt file to read the current high score
        with open("high_score.txt", "r") as file:
            high_score = int(file.read())  # Read the file content and convert to integer
    except FileNotFoundError:
        high_score = 0  # If the file doesn't exist, set high score to 0

    # Compare the current score with the stored high score
    if cumulative_score > high_score:
        # If the current score is higher, update the high score file
        with open("high_score.txt", "w") as file:
            file.write(str(cumulative_score))  # Write the new high score to the file
        print(f"\n🎉 You've achieved a new high score! Your cumulative score this session is: {cumulative_score}! 🎉")
    else:
        # If not, just print the current score and high score
        print(f"\nYour cumulative score this session is: {cumulative_score}.")
        print(f"The all-time high score remains: {high_score}.")

# Function to display the high score at the start of the game
def display_high_score():
    try:
        # Try opening the high_score.txt file to read the current high score
        with open("high_score.txt", "r") as file:
            high_score = int(file.read())  # Read and convert the high score to an integer
        print(f"\n🌟 High Score: {high_score} 🌟")  # Display the high score
    except FileNotFoundError:
        # If the file is not found (first game), notify the player
        print("\nNo high score recorded yet!")

# Function to print game instructions and initialize settings
def initialize_game():
    os.system("cls" if os.name == "nt" else "clear")  # Clear the screen for a fresh start
    print("\n" + "?" * 40)  # Print a welcome message decoration
    print("WELCOME TO THE GUESSING GAME!")  # Display game title
    print("?" * 40)  # Print closing decoration

# Function to set difficulty based on player input
def set_difficulty():
    print("\nSelect Difficulty Level:")  # Ask the player to choose a difficulty
    print("1. Easy (1-100, 10 attempts)")  # Easy difficulty option
    print("2. Medium (1-200, 7 attempts)")  # Medium difficulty option
    print("3. Hard (1-300, 5 attempts)")  # Hard difficulty option
    print("4. Custom (Choose your own range and attempts)")  # Custom difficulty option
    return get_integer_input("Enter your choice (1/2/3/4): ", 1, 4)  # Get and return the user's choice

# Function to set range and attempts based on difficulty choice
def difficulty_settings(difficulty):
    if difficulty == 1:
        return 100, 10  # Easy mode: range 1-100, 10 attempts
    elif difficulty == 2:
        return 200, 7  # Medium mode: range 1-200, 7 attempts
    elif difficulty == 3:
        return 300, 5  # Hard mode: range 1-300, 5 attempts
    elif difficulty == 4:
        max_range = get_integer_input("Enter the maximum range: ", 10, 10000)  # Custom range input
        max_attempts = get_integer_input("Enter the number of attempts: ", 1, 20)  # Custom attempts input
        return max_range, max_attempts  # Return custom settings

# Main game function that controls the flow of the guessing game
def guessing_game():
    score = 0  # Initialize player's score
    streak = 0  # Initialize winning streak
    is_first_game = True  # Flag to track if it's the first game

    while True:  # Start an infinite loop for the game
        if is_first_game:
            initialize_game()  # Initialize game with instructions
            display_high_score()  # Display the high score at the start
            is_first_game = False  # Set flag to False after the first round

        difficulty = set_difficulty()  # Get the player's difficulty choice
        max_range, max_attempts = difficulty_settings(difficulty)  # Get the settings based on the difficulty
        number_to_guess = random.randint(1, max_range)  # Generate the random number to guess
        attempts = 0  # Initialize attempt counter

        print(f"\nI've chosen a number between 1 and {max_range}. You have {max_attempts} attempts. Let's begin!")

        # Main guessing loop
        while attempts < max_attempts:
            guess = get_integer_input(f"Enter your guess (1-{max_range}): ", 1, max_range)  # Get the player's guess
            attempts += 1  # Increment the attempt counter

            # Check if the guess is too low, too high, or correct
            if guess < number_to_guess:
                proximity_hint = abs(number_to_guess - guess)
                if proximity_hint <= max_range * 0.1:
                    print(f"You're very close! But it's low. {max_attempts - attempts} attempts left.")
                else:
                    print(f"Too low! {max_attempts - attempts} attempts left.")
            elif guess > number_to_guess:
                proximity_hint = abs(guess - number_to_guess)
                if proximity_hint <= max_range * 0.1:
                    print(f"You're very close! But it's high. {max_attempts - attempts} attempts left.")
                else:
                    print(f"Too high! {max_attempts - attempts} attempts left.")
            else:
                streak += 1  # Increment streak when the player guesses correctly
                score += (max_attempts - attempts + 1) * 10  # Calculate score based on attempts used
                print(f"\n🎉 That's correct! You guessed the number in {attempts} attempts! 🎉")
                print(f"Your current score is: {score}!")
                print(f"You have a winning streak of: {streak} 🎯")

                if streak % 5 == 0:
                    print(f"🔥 Amazing! You're on a streak of {streak}! Extra 10 points!")
                    score += 10  # Add bonus points for a streak
                break  # Exit guessing loop if the guess is correct

        # If the player runs out of attempts without guessing correctly
        if attempts == max_attempts and guess != number_to_guess:
            streak = 0  # Reset streak after a loss
            print(f"\nSorry, you've used all your attempts. The number was {number_to_guess}.")
            print(f"Your final score is: {score}")

        play_again = input("Would you like to play again? (yes/no): ").strip().lower()  # Ask the player to play again

        if play_again == "yes":
            os.system("cls" if os.name == "nt" else "clear")  # Clear the screen for a fresh start
        else:
            save_high_score(score)  # Save the high score when the game ends
            display_goodbye_message()  # Display goodbye message
            break  # Exit the game loop

if __name__ == "__main__":
    guessing_game()  # Start the game if this script is executed directly
