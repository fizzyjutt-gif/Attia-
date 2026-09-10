import random


def guessing_game():
    print("================================")
    print("       GUESSING GAME")
    print("================================")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            elif guess < secret_number:
                print("Too Low! Try again.")
            elif guess > secret_number:
                print("Too High! Try again.")
            else:
                print("Correct! 🎉")
                print(f"You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    guessing_game()
