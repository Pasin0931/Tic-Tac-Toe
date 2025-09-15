"""
Tic Tac Toe Game (customizable board size).

This program allows two players to play Tic Tac Toe
on an n x n board (size between 3 and 10).
Players choose their own symbols and take turns
until one wins or the game ends in a draw.
"""


def ask_user():
    """
    Ask the user for board size and player symbols.

    Returns:
        tuple: (board_size, player1_symbol, player2_symbol)
    """
    while True:
        try:
            while True:
                board_size = int(
                    input("Enter board size n for n x n board (3-10): ")
                )
                if board_size >= 3 and board_size <= 10:
                    break
                else:
                    print(invalid)
            break
        except ValueError:
            print(invalid)

    while True:
        p1 = input("Enter Player 1's symbol (a single letter): ")
        if len(p1) == 1:
            break
        else:
            print(invalid)

    while True:
        p2 = input(
            "Enter Player 2's symbol (a single letter, different from 'I'): "
        )
        if len(p2) == 1:
            if p1 != p2:
                break
            else:
                print(invalid)
        else:
            print(invalid)

    return board_size, p1, p2


def create_table(board_size):
    """
    Create the initial game table with numbered cells.

    Args:
        board_size (int): Size of the board (n x n).

    Returns:
        tuple: (table, next_number)
            table (list of lists): 2D list representing the game board.
            next_number (int): Next number after filling the table.
    """
    row = [[] * row for row in range(board_size)]

    count = 1
    for sec in row:
        for col in range(board_size):
            sec.append(count)
            count += 1

    return row, count


def display_table(table):
    """
    Print the current state of the game board.

    Args:
        table (list of lists): The current game board.
    """
    plus_ = "+" * (len(table) + 1)

    if len(str(maxi)) == 1:
        ml = 3
    elif len(str(maxi)) == 2:
        ml = 4
    else:
        ml = 4

    d_dash = "-" * ml
    r_dash = d_dash.join(plus_)
    for row in table:
        print(r_dash)
        print("|", end="")
        for col in row:
            if ml == 3:
                print(f"{col:^3}", end="")
            else:
                print(f"{col:^4}", end="")
            print("|", end="")
        print()
    print(r_dash)


def player_turn(player, table):
    """
    Handle a single player's turn by placing their symbol on the board.

    Args:
        player (str): The player's symbol.
        table (list of lists): The current game board.
    """
    max_table_value = board_size ** 2
    state_pass = False

    while not state_pass:
        try:
            player_move = int(
                input(
                    f"Player '{player}', enter your move position "
                    f"(1-{max_table_value}): "
                )
            )
        except ValueError:
            print(invalid)
            continue

        if player_move < 1 or player_move > max_table_value:
            print(out_of_range)
            continue

        for row in table:
            if player_move in row:
                idx = row.index(player_move)
                row[idx] = player
                state_pass = True
                break

        if not state_pass:
            print("That position is already taken. Try again.")


def check_win(player):
    """
    Check if a given player has won the game.

    Args:
        player (str): The player's symbol.

    Returns:
        bool: True if the player has won, False otherwise.
    """
    for row in table_xox:
        if all(cell == player for cell in row):
            return True

    for col in range(board_size):
        if all(table_xox[row][col] == player for row in range(board_size)):
            return True

    if all(table_xox[i][i] == player for i in range(board_size)):
        return True

    if all(
        table_xox[i][board_size - 1 - i] == player
        for i in range(board_size)
    ):
        return True

    return False


def check_draw():
    """
    Check if the game is a draw (all cells are filled with no winner).

    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    for row in table_xox:
        for cell in row:
            if isinstance(cell, int):
                return False
    return True


# Main part
invalid = "Invalid input. Please enter a number."
out_of_range = "Position out of range. Please try again."

board_size, player_1, player_2 = ask_user()
table_xox, count_number_in_table = create_table(board_size)
maxi = max(table_xox[-1])

win = False
player_1_turn = True

while not win:
    display_table(table_xox)

    if player_1_turn:
        player_turn(player_1, table_xox)
        if check_draw():
            display_table(table_xox)
            print("It's a draw!")
            break
        if check_win(player_1):
            display_table(table_xox)
            print(f"Player '{player_1}' wins!")
            break
        player_1_turn = False

    else:
        player_turn(player_2, table_xox)
        if check_draw():
            display_table(table_xox)
            print("It's a draw!")
            break
        if check_win(player_2):
            display_table(table_xox)
            print(f"Player '{player_2}' wins!")
            break
        player_1_turn = True
