#!/usr/bin/python3

""" Rotate a 2D matrixrix 90 Degrees Clockwise"""


def rotate_2d_matrix(matrix):
    """ Function to rotate a matrixrix 90 degree clockwise
    """

    if not matrix or not len(matrix):
        return

    N = len(matrix)

    for i in range(N):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for i in range(N):
        for j in range(N // 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][N - j - 1]
            matrix[i][N - j - 1] = temp
