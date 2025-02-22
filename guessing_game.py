import random


# Function to get valid integer input within a specified range
def get_integer_input(prompt, min_value, max_value, allow_cancel=False, simulated_input=None):
    if simulated_input:
        return simulated_input.pop(0)
    while True:
        user_input = input(prompt).strip().lower()
        if allow_cancel and user_input == "cancel":
            return "cancel"
        if user_input.isdigit() and min_value <= int(user_input) <= max_value:
            return int(user_input)
        print(f"Please enter a number between {min_value} and {max_value}.")


# Function to display and save high scores
def handle_high_score(score=None):
    try:
        with open("high_score.txt", "r+") as file:
            high_score = int(file.read().strip() or 0)
            if score is not None and score > high_score:
                file.seek(0)
                file.write(str(score))
                print(f"\n🎉 New High Score! Your score: {score}! 🎉")
            return high_score
    except FileNotFoundError:
        if score is not None:
            with open("high_score.txt", "w") as file:
                file.write(str(score))
        return 0


# Function to initialize game
def initialize_game():
    print("\n" + "?" * 50 + "\nWELCOME TO THE GUESSING GAME!\n" + "?" * 50)
    print("\n🌟 High Score:", handle_high_score(), "🌟\n")


# Function to select difficulty
def select_difficulty(simulated_input=None):
    print(
        "Select Difficulty Level:\n1. Easy (1-100, 10 attempts)\n2. Medium (1-200, 7 attempts)\n3. Hard (1-300, 5 attempts)")
    return get_integer_input("Please enter your choice (1-3): ", 1, 3, False, simulated_input)


# Main game function
def guessing_game(simulated_input=None):
    score, streak = 0, 0
    while True:
        initialize_game()
        difficulty = select_difficulty(simulated_input)
        max_range, max_attempts = [(100, 10), (200, 7), (300, 5)][difficulty - 1]
        number, attempts = random.randint(1, max_range), 0
        print(f"\nI've chosen a number between 1 and {max_range}. You have {max_attempts} attempts.")

        while attempts < max_attempts:
            guess = get_integer_input(f"Enter guess (1-{max_range}): ", 1, max_range, True, simulated_input)
            if guess == "cancel":
                print("Returning to main menu...\n")
                break
            attempts += 1
            difference = abs(guess - number)

            if guess == number:
                streak += 1
                score += (max_attempts - attempts + 1) * 10
                print(f"\n🎉 Correct! You guessed in {attempts} attempts! Score: {score}, Streak: {streak} 🎯")
                if streak % 5 == 0:
                    print(f"🔥 Streak bonus! Extra 10 points!")
                    score += 10
                break
            print(
                f"{'Too low' if guess < number else 'Too high'} but you're close! {max_attempts - attempts} attempts left." if difference <= 5 else f"{'Too low' if guess < number else 'Too high'}! {max_attempts - attempts} attempts left.")

        if guess == "cancel":
            continue  # Restart game without prompt

        if attempts == max_attempts:
            print(f"\nOut of attempts! The number was {number}. Final score: {score}")
            streak = 0

        if (simulated_input.pop(0) if simulated_input else input("Play again? (yes/no): ").strip().lower()) != "yes":
            handle_high_score(score)
            print("\nThanks for playing! See ya next time!")
            break


if __name__ == "__main__":
    guessing_game()
