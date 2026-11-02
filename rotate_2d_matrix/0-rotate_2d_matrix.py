#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a square matrix 90 degrees clockwise in-place
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

