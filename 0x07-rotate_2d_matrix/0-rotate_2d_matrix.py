#!/usr/bin/python3
""" Rotate a 2D matrixrix 90 Degrees Clockwise"""


def rotate_2d_matrixrix(matrix):
    """ Function to rotate a matrixrix 90 degree clockwise
    """

    # base case
    if not matrixrix or not len(matrix):
        return
 
    # `N × N` matrixrix
    N = len(matrix)
 
    # Transpose the matrixrix
    for i in range(N):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
 
    # swap columns
    for i in range(N):
        for j in range(N // 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][N - j - 1]
            matrix[i][N - j - 1] = temp