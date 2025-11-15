import art
import random

def clear():
    print("\n" * 100)

def game():
    print(art.logo)
    print("Welcome to the number guessing game.")

    number_to_guess = random.randint(1, 100)

    def game_logic():
        game_difficulty = input("What difficulty do you want? (Easy/Medium/Hard): \n").lower()

        attempts = {
            "easy": 15,
            "medium": 10,
            "hard": 5
        }

        if game_difficulty not in attempts:
            retry = input("Invalid input. Try again? (y/n): ")
            if retry == "y":
                return game_logic()
            else:
                print("Bye. Have a great time.")
                exit()

        remaining_attempts = attempts[game_difficulty]

        while remaining_attempts > 0:
            print(f"You have {remaining_attempts} attempts remaining.")
            user_guess = int(input("What is your guess? "))

            if user_guess == number_to_guess:
                print(f"You guessed correctly! The number was {number_to_guess}.")
                exit()

            elif user_guess > number_to_guess:
                print("Too high.")

            else:
                print("Too low.")

            remaining_attempts -= 1

        retry = input("You're out of attempts. Do you want to try again? (y/n): ")
        if retry == "y":
            clear()
            return game_logic()
        else:
            print("Bye. Have a great time.")
            exit()

    game_logic()

game()