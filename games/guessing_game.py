import random

def guessing_game():
    print("Guess the number!")

    secret_number = random.randrange(101)
    guess_count = 0

    while True:
        guess = input("Input your guess: ")

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter an integer.")
            continue

        guess_count += 1
        print(f"You guessed: {guess}")

        if guess == secret_number:
            print(f"You win! It took you {guess_count} guesses.")
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again == 'yes':
                guessing_game()
            else:
                print("Thanks for playing! Goodbye!")
            break
        elif guess < secret_number:
            print("Too small!")
        else:
            print("Too big!")

if __name__ == '__main__':
    guessing_game()
