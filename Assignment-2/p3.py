def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i) == 0:
            return False
    return n > 1

def get_prime_factors(n):
    prime_factors = [
        i for i in range(1, n)
        if (n % i == 0 and is_prime(i)) 
    ]
    return prime_factors

N = int(input("Enter a number: "))
prime_factors = get_prime_factors(N)

if (prime_factors):
    print(f"The prime factors of {N} are: ")
    print(*prime_factors, sep=", ")

else:
    print(f"There are no prime factors of {N}")