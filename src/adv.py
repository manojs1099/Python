import random
import textwrap
from room import Room
from player import Player  # Import the Player class

# Include your guessing game and rock-paper-scissors functions
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
            break
        elif guess < secret_number:
            print("Too small!")
        else:
            print("Too big!")

def rock_paper_scissors():
    def load_results():
        try:
            with open("history.txt", "r") as file:
                history = file.read().split(",")
                return [int(result) for result in history]
        except FileNotFoundError:
            return [0, 0, 0]

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

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main
# Make a new player object that is currently in the 'outside' room.
player = Player("Adventurer", room['outside'])

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# * If the user enters a cardinal direction, attempt to move to the room there.
#   Print an error message if the movement isn't allowed.
# * If the user enters "q", quit the game.
while True:
    current_room = player.current_room
    print(f"\n{current_room.name}\n")
    print(textwrap.fill(current_room.description, width=50))
    command = input("\nEnter a direction (n, s, e, w) or a command (q to quit, g for guessing game, r for rock-paper-scissors): ").strip().lower()

    if command == 'q':
        print("Thanks for playing!")
        break
    elif command in ['n', 's', 'e', 'w']:
        direction_attr = f"{command}_to"
        if hasattr(current_room, direction_attr):
            player.current_room = getattr(current_room, direction_attr)
        else:
            print("You can't go that way!")
    elif command == 'g':
        guessing_game()
    elif command == 'r':
        rock_paper_scissors()
    else:
        print("Invalid command.")
