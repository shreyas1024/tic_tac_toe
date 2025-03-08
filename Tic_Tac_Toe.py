def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        row, col = map(int, input(f"Player {players[turn % 2]} (row col): ").split())

        if board[row][col] == " ":
            board[row][col] = players[turn % 2]
            if check_winner(board, players[turn % 2]):
                print_board(board)
                print(f"Player {players[turn % 2]} wins!")
                break
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            turn += 1
        else:
            print("Cell already taken! Try again.")

tic_tac_toe()
