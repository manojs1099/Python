import math
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def get_user_input(board):
    while True:
        try:
            user_input = input("Enter row and column (0, 1, 2) or 'q' to quit: ").strip()
            if user_input.lower() == 'q':
                return user_input, user_input
            row, col = map(int, user_input.split())
            if row in [0, 1, 2] and col in [0, 1, 2] and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space or 'q' to quit. Try again.")

def minimax(board, depth, is_maximizing):
    if check_winner(board, "X"):
        return 1
    if check_winner(board, "O"):
        return -1
    if all([cell != " " for row in board for cell in row]):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "X"
                    score = minimax(board, depth + 1, False)
                    board[r][c] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "O"
                    score = minimax(board, depth + 1, True)
                    board[r][c] = " "
                    best_score = min(score, best_score)
        return best_score

def get_computer_move(board):
    if random.random() < 0.5: 
        best_score = -math.inf
        best_move = None
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "X"
                    score = minimax(board, 0, False)
                    board[r][c] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (r, c)
        return best_move
    else: 
        available_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
        return random.choice(available_moves)

def tic_tac_toe():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "O"  
        moves = 0

        print("Player O will start the game.\n")

        while True:
            print_board(board)
            if current_player == "X":
                print(f"Player {current_player}'s turn (Computer).")
                row, col = get_computer_move(board)
            else:
                print(f"Player {current_player}'s turn (You).")
                row, col = get_user_input(board)
                if row == 'q' or col == 'q':
                    print("Thanks for playing! Goodbye.")
                    return

            if board[row][col] == " ":
                board[row][col] = current_player
                moves += 1
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break
                elif moves == 9:
                    print_board(board)
                    print("It's a tie!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                if current_player == "O":
                    print("Cell is already occupied. Try again.")

        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    tic_tac_toe()
