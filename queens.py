N = 8

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_queens(board, row):
    if row == N:
        print_board(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(board, row + 1):
                return True
            board[row] = -1  # Backtrack

    return False


def print_board(board):
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


board = [-1] * N
solve_queens(board, 0)
