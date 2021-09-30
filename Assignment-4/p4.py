def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i == 0): 
            return False
    return n > 1

get_primes = lambda low, high: [i for i in range(low, high + 1) if is_prime(i)]
def twin_primes(low, high):
    primes = get_primes(low, high)
    return [
        (primes[i], primes[i + 1]) for i in range(len(primes) - 1) 
        if primes[i] + 2 == primes[i + 1]
    ]

low, high = map(int, input("Enter the range (inclusive): ").split())
print(*twin_primes(low, high), sep=',\n')