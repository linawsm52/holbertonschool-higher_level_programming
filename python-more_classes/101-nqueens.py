#!/usr/bin/python3
"""
N queens solver.

Usage: nqueens N
Prints all solutions to the N queens problem.
Only sys module is allowed.
"""

import sys


def print_usage_and_exit():
    """Print usage message and exit with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def validate_n():
    """Validate command line argument N and return it as int."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def solve_nqueens(n):
    """
    Solve N queens using backtracking.
    Returns a list of solutions, each solution is a list of [row, col].
    """
    solutions = []
    cols = set()
    diag1 = set()  # r - c
    diag2 = set()  # r + c
    board = [-1] * n  # board[r] = c

    def backtrack(r):
        if r == n:
            sol = [[i, board[i]] for i in range(n)]
            solutions.append(sol)
            return

        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue

            board[r] = c
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)

            backtrack(r + 1)

            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)
            board[r] = -1

    backtrack(0)
    return solutions


def main():
    n = validate_n()
    for sol in solve_nqueens(n):
        print(sol)


if __name__ == "__main__":
    main()
