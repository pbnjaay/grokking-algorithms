from termcolor import colored


NIL = ''
X = 'X'
O = 'O'


def cell(player):
    if player == NIL:
        return ' '
    color = 'red' if player == X else 'green'
    return colored(player, color)


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


def is_over(board):
    check = False
    for row in board:
        if row[0].strip() and row[1].strip() and row[2].strip():
            check = True
        else:
            check = False
    return check


def display_board():
    line = '---+---+---'
    for row in board:
        print(f' {cell(row[0])} | {cell(row[1])} | {cell(row[2])}')
        print(line)


def get_position(label):
    while True:
        try:
            value = int(input(f'Enter {label} (0-2): '))
            if value < 0 or value > 2:
                raise ValueError()
            return value
        except ValueError:
            print('Invalid input')


def marks(player, row, col):
    board[row][col] = player


def get_move(player):
    while True:
        row = get_position('row')
        col = get_position('col')
        if board[row][col]:
            print('Spot already taken!')
        else:
            marks(player, row, col)
            break


def run(board):
    display_board()
    current_player = X
    while True:
        print(f"Player {current_player}'s turn")
        get_move(current_player)
        display_board()

        if check_winner(board):
            print(f"Player {current_player} wins !")
            break

        if is_over(board):
            print('Draw !')
            break

        current_player = O if current_player == X else X


if __name__ == '__main__':
    board = [[NIL, NIL, NIL], [NIL, NIL, NIL], [NIL, NIL, NIL]]
    run(board)
