#!/usr/bin/python3
"""Module for making change."""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total."""

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(
                    dp[amount],
                    dp[amount - coin] + 1
                )

    if dp[total] == float('inf'):
        return -1

    return dp[total]