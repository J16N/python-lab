def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i == 0): 
            return False
    return n > 1

palindromic_prime = lambda low, high: [
    i for i in range(low, high + 1)
    if (is_prime(i) and str(i) == str(i)[::-1])    
]

low, high = map(int, input("Enter the range (inclusive): ").split())
print(*palindromic_prime(low, high), sep=', ')