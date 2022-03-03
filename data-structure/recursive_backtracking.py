
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def print_board(board):
    n = len(board[0])
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print('\n')


# First choose where to put the first queen, the first queen lie on the col 0:
def create_board(n):
    return [[0 for i in range(n)] for j in range(n)]


def is_safe(board, n):
    for i in range(n):



def place_queen(board, col, row):
