WINNING_LINES = [
    (1, 2, 3),  # rows
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),  # columns
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),  # diagonals
    (3, 5, 7),
]


def create_board():
    """Return a new board whose cells are labelled 1 through 9."""
    return [str(number) for number in range(1, 10)]


def display_board(board):
    """Print the current 3 x 3 board."""
    print()
    for row in range(3):
        start = row * 3
        print(" " + " | ".join(board[start:start + 3]))
        if row < 2:
            print("---+---+---")
    print()


def check_win(board, player):
    """Return the winning line if player has won; otherwise return None."""
    for line in WINNING_LINES:
        if all(board[position - 1] == player for position in line):
            return line
    return None


def check_draw(board):
    """Return True when every cell is occupied and nobody has won."""
    return all(cell in ("X", "O") for cell in board)


def take_move(board, player):
    """
    Ask the current player for a move.
    Return True after a valid move, or False if the move was invalid.
    Invalid input leaves the board and turn unchanged.
    """
    raw_position = input(f"Player {player}, enter a position (1-9): ").strip()

    try:
        position = int(raw_position)
    except ValueError:
        print("Invalid position. Enter a number from 1 to 9.")
        return False

    if position < 1 or position > 9:
        print("Invalid position. Enter a number from 1 to 9.")
        return False

    if board[position - 1] in ("X", "O"):
        print("Position is already taken. Choose another position.")
        return False

    board[position - 1] = player
    return True


def play_game():
    """Play one complete game."""
    board = create_board()
    current_player = "X"

    print("\nWelcome to Tic-Tac-Toe!")
    print("Choose a position using the numbers shown on the board.")
    display_board(board)

    while True:
        # The turn changes only after a valid move.
        if not take_move(board, current_player):
            continue

        display_board(board)

        winning_line = check_win(board, current_player)
        if winning_line:
            line_text = "-".join(str(position) for position in winning_line)
            print(f"Player {current_player} wins!")
            print(f"Winning line: {line_text}")
            break

        if check_draw(board):
            print("Board is full after 9 moves.")
            print("It's a draw! No moves left.")
            break

        current_player = "O" if current_player == "X" else "X"


def main():
    """Run games until the players choose not to play again."""
    while True:
        play_game()
        answer = input("Play again? (y/n): ").strip().lower()
        if answer != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()