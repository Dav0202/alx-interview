#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    """
    min operation function
    """
    if not isinstance(n, int):
        return 0

    min_op = 0
    char = 2
    while (char <= n):
        if not (n % char):
            n = int(n / char)
            min_op += char
            char = 1
        char += 1
    return min_op
