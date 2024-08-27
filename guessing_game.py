import random

def get_integer_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def guessing_game():
    while True:
        # Select difficulty
        print("Select Difficulty Level:")
        print("1. Easy (1-100, 10 attempts)")
        print("2. Medium (1-200, 7 attempts)")
        print("3. Hard (1-500, 5 attempts)")
        difficulty = get_integer_input("Enter your choice (1/2/3): ", 1, 3)

        if difficulty == 1:
            number_to_guess = random.randint(1, 100)
            max_attempts = 10
            max_range = 100
        elif difficulty == 2:
            number_to_guess = random.randint(1, 200)
            max_attempts = 7
            max_range = 200
        else:
            number_to_guess = random.randint(1, 500)
            max_attempts = 5
            max_range = 500

        attempts = 0

        print("Welcome to the Guessing Game!")
        print(f"I have chosen a number between 1 and {max_range}. Can you guess it?")
        print(f"You have a maximum of {max_attempts} attempts to guess the number.")

        while attempts < max_attempts:
            guess = get_integer_input(f"Enter your guess (between 1 and {max_range}): ", 1, max_range)
            attempts += 1

            if guess < number_to_guess:
                print(f"Too low! You have {max_attempts - attempts} attempts left. Try again.")
            elif guess > number_to_guess:
                print(f"Too high! You have {max_attempts - attempts} attempts left. Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break

        if attempts == max_attempts and guess != number_to_guess:
            print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    guessing_game()
