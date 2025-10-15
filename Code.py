import random

def generate_random_number(min_range=1, max_range=20):
    return random.randint(min_range, max_range)

def get_user_guess():
    while True:
        try:
            return int(input("Take a guess (make it count!): "))
        except ValueError:
            print("Please enter a valid number.")

def evaluate_guess(guess, target_number):
    if guess < target_number:
        print("Too low")
        return False
    elif guess > target_number:
        print("Too high")
        return False
    else:
        print("Correct! Someone's been practicing.")
        return True

def play_guessing_game(min_range=1, max_range=20, max_attempts=5):
    target_number = generate_random_number(min_range, max_range)
    attempts = 0
    print(f"\nI'm thinking of a number between {min_range} and {max_range}.")
    print(f"You’ve got {max_attempts} guesses. No pressure.\n")


    while attempts < max_attempts:
        guess = get_user_guess()
        attempts += 1
        if evaluate_guess(guess, target_number):
            break
    else:
        print(f"\nOof. You've used all {max_attempts} attempts! The number was {target_number}")
        print("But hey, you gave it a solid shot.")

    print("\nTotal attempts:", attempts)
    print("Thanks for playing! Come back soon :)")

if __name__ == "__main__":
    play_guessing_game()

