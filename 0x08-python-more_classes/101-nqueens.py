#!/usr/bin/python3
# 101-nqueens.py
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys

def init_board(n):
    return [[" " for _ in range(n)] for _ in range(n)]

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == "Q":
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    return True

def solve_nqueens(n):
    def backtrack(board, col):
        if col == n:
            solutions.append(["".join(row) for row in board])
            return
        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = "Q"
                backtrack(board, col + 1)
                board[i][col] = " "

    board = init_board(n)
    solutions = []
    backtrack(board, 0)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solutions = solve_nqueens(N)
    for solution in solutions:
        for row in solution:
            print(row)
        print()
