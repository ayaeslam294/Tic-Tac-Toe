import random
import os

def print_board(board):
    # Clear screen safely for Windows and Linux
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
    print()

def get_available_positions(board):
    positions = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', 'O']:
                positions.append((r, c))
    return positions

def getWinner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
    # Check columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

# Initialize the board
board = [['1','2','3'], ['4','5','6'], ['7','8','9']]
dic = {
    '1': (0, 0), '2': (0, 1), '3': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '7': (2, 0), '8': (2, 1), '9': (2, 2)
}

turn = True  # Player starts first
result = None

while True:
    print_board(board)
    positions = get_available_positions(board)
    if len(positions) == 0:
        break

    if turn:  # Human
        choice = input("Enter position (1-9): ")
        if choice not in dic:
            print("Invalid choice, try again.")
            input("Press Enter to continue...")
            continue
        r, c = dic[choice]
        if board[r][c] in ['X', 'O']:
            print("That spot is already taken.")
            input("Press Enter to continue...")
            continue
        board[r][c] = 'X'
    else:  # Computer
        print("Computer is playing...")
        r, c = random.choice(positions)
        board[r][c] = 'O'

    result = getWinner(board)
    if result is not None:
        print_board(board)
        print(f"🎉 Winner: {result}")
        break

    turn = not turn

if result is None:
    print_board(board)
    print("🤝 It's a tie!")
