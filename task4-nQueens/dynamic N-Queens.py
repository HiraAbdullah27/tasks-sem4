def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append([row[:] for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0  # backtrack

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    print(f"Total solutions for {n}-Queens: {len(solutions)}")
    for sol in solutions:
        print_board(sol)

# Example usage:
n_queens(4)  # You can change the number to test other values


