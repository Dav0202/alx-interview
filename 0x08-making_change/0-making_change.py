def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    i = total + 1

    data = {0: 0}

    for i in range(1, total + 1):
        data[i] = i
        for coin in coins:
            current = i - coin
            if current < 0:
                continue
            
            data[i] = min(data[current] + 1, data[i])

    if data[total] == total + 1:
        return -1

    return data[total]
