#!/usr/bin/python3
"""
Making Changes
"""

def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    i = total
    count = 0
    index = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while i > 0:
        if index >= n:
            return -1
        if i - sorted_coins[index] >= 0:
            i -= sorted_coins[index]
            count += 1
        else:
            index += 1
    return count
