#!/usr/bin/python3
"""0-nqueens module"""

import sys


def print_usage():
    """Print usage message"""
    print("Usage: nqueens N")


def validate_args(args):
    """Validate arguments passed to the program"""
    if len(args) != 2:
        print_usage()
        sys.exit(1)

    try:
        N = int(args[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    return N


def is_safe(board, row, col):
    """Check if a queen can be placed at a given row and column"""
    for i in range(row):
        if board[i] == col:
            return False

    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i] == j:
            return False

    return True


def solve_nqueens_util(N, board, row):
    """Solve the N-queens problem using backtracking"""
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens_util(N, board, row + 1)
            # Backtrack
            board[row] = -1


def solve_nqueens(N):
    """Solve the N-queens problem"""
    board = [-1] * N
    solve_nqueens_util(N, board, 0)


if __name__ == "__main__":
    N = validate_args(sys.argv)
    solve_nqueens(N)
