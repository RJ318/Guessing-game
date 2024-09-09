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

def display_welcome_message():
    print("\n" + "="*40)
    print("WELCOME TO THE GUESSING GAME!")
    print("="*40)

def display_goodbye_message():
    print("\n" + "="*40)
    print("Thank you for playing! Goodbye!")
    print("="*40)

def guessing_game():
    score = 0
    streak = 0

    while True:
        display_welcome_message()
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

        print(f"\nI've chosen a number between 1 and {max_range}.")
        print(f"You have {max_attempts} attempts. Let's begin!")

        while attempts < max_attempts:
            guess = get_integer_input(f"Enter your guess (between 1 and {max_range}): ", 1, max_range)
            attempts += 1

            if guess < number_to_guess:
                proximity_hint = abs(number_to_guess - guess)
                if proximity_hint <= max_range * 0.1:
                    print(f"Very close! Too low, {max_attempts - attempts} attempts left.")
                else:
                    print(f"Too low! {max_attempts - attempts} attempts left.")
            elif guess > number_to_guess:
                proximity_hint = abs(guess - number_to_guess)
                if proximity_hint <= max_range * 0.1:
                    print(f"Very close! Too high, {max_attempts - attempts} attempts left.")
                else:
                    print(f"Too high! {max_attempts - attempts} attempts left.")
            else:
                streak += 1
                score += (max_attempts - attempts + 1) * 10  # Higher points for fewer attempts
                print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts.")
                print(f"Your current score is: {score}")
                print(f"Winning streak: {streak} 🎯")
                break

        if attempts == max_attempts and guess != number_to_guess:
            streak = 0
            print(f"\nSorry, you've used all your attempts. The number was {number_to_guess}.")
            print(f"Your final score is: {score}")

        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            display_goodbye_message()
            break

if __name__ == "__main__":
    guessing_game()
