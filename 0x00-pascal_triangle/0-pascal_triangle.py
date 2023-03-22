#!/usr/bin/python3
""" Module for calculating Pascal Triangle """

def pascal_triangle(n):
    """ Function for creating a pascal triangle as a list of lists
    """
    if n <= 0:
        return ([])

    tmp = [[1]]
    for i in range(1, n):
        row = [1]
        new = tmp[i - 1]
        for u in range(len(new)):
            new = new[u] + new[u + 1] if u != len(new) - 1 else 1
            row.append(new)
        tmp.append(row)
    return tmp
