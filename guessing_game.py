import random


def guessing_game():
    number_to_guess = random.randint(1, 200)  # Random number between 1 and 200
    attempts = 0
    max_attempts = 10

    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 200. Can you guess it?")
    print(f"You have a maximum of {max_attempts} attempts to guess the number.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 200:
                print("Please guess a number within the range of 1 to 200.")
            elif guess < number_to_guess:
                print(f"Too low! You have {max_attempts - attempts} attempts left. Try again.")
            elif guess > number_to_guess:
                print(f"Too high! You have {max_attempts - attempts} attempts left. Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

    if attempts == max_attempts and guess != number_to_guess:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")


if __name__ == "__main__":
    guessing_game()
