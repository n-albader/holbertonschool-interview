#!/usr/bin/python3
"""Solve the N queens puzzle using backtrackin"""

import sys


def solve_nqueens(n):
    """Print all solutions to the N queens puzzle"""
    solutions = []
    positions = []

    def backtrack(row):
        """Place queens one row at a time"""
        if row == n:
            solutions.append([[r, positions[r]] for r in range(n)])
            return

        for col in range(n):
            valid = True

            for prev_row in range(row):
                prev_col = positions[prev_row]

                if (prev_col == col or
                        abs(prev_col - col) == abs(prev_row - row)):
                    valid = False
                    break

            if valid:
                positions.append(col)
                backtrack(row + 1)
                positions.pop()

    backtrack(0)

    for solution in solutions:
        print(solution)


def main():
    """Validate arguments and solve the puzzle"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
