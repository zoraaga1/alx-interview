def isWinner(x, nums):
    def sieve(n):
        """ Helper function to compute prime numbers up to n using Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulates a single game of choosing primes and removing primes and their multiples """
        primes = sieve(n)
        prime_set = set(primes)
        turn = 0  # 0 for Maria's turn, 1 for Ben's turn
        
        while primes:
            current_prime = primes.pop(0)
            if current_prime in prime_set:
                multiples = set(range(current_prime, n + 1, current_prime))
                prime_set -= multiples
                primes = [p for p in primes if p in prime_set]
                turn = 1 - turn
        
        # If the last turn was Maria's (0), Ben wins (1), and vice versa
        return turn  # Return the winner: 1 for Ben, 0 for Maria
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if n < 2:
            ben_wins += 1
        else:
            winner = play_game(n)
            if winner == 0:
                maria_wins += 1
            else:
                ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
