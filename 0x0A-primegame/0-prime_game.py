#!/usr/bin/python3
""" Prime Game Module """


def isWinner(x, nums):
    """Determines the winner of the prime game"""
    if x < 1 or not nums:
        return None

    max_n = max(nums)

    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_n + 1, i):
                sieve[j] = False

    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
