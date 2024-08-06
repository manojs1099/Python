import random

# File I/O functions for historical results
def load_results():
    try:
        with open("history.txt", "r") as file:
            history = file.read().split(",")
            return [int(result) for result in history]
    except FileNotFoundError:
        return [0, 0, 0]  # Default to zero if the file does not exist

def save_results(wins, ties, losses):
    with open("history.txt", "w") as file:
        file.write(f"{wins},{ties},{losses}")

def get_user_choice():
    while True:
        try:
            choice = int(input("[1] Rock  [2] Paper  [3] Scissors  [9] Quit\n"))
            if choice in [1, 2, 3, 9]:
                return choice
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        return "win"
    else:
        return "loss"

def main():
    # Load historical results
    results = load_results()
    wins, ties, losses = results

    print("Welcome to Rock, Paper, Scissors!")
    print(f"Wins: {wins}, Ties: {ties}, Losses: {losses}")
    print("Please choose to continue...")

    while True:
        computer = random.randint(1, 3)
        user = get_user_choice()

        if user == 9:
            break

        outcomes = {
            1: "Rock",
            2: "Paper",
            3: "Scissors"
        }

        outcome = determine_winner(user, computer)

        if outcome == "tie":
            print(f"Computer chose {outcomes[computer]}...tie!")
            ties += 1
        elif outcome == "win":
            print(f"Computer chose {outcomes[computer]}...you win :)")
            wins += 1
        else:
            print(f"Computer chose {outcomes[computer]}...computer wins :(")
            losses += 1

        print(f"Wins: {wins}, Ties: {ties}, Losses: {losses}")
        print("Please choose to continue...")

    save_results(wins, ties, losses)
    print("Game over. Results have been saved.")

if __name__ == '__main__':
    main()
