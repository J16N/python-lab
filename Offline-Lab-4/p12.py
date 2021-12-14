from math import sqrt
from collections import deque

def circPerm(n):
    d = deque(n)
    permutations = []
    for _ in range(len(n)):
        d.rotate()
        permutations.append(
            int(''.join(d))
        )
    return permutations

def isPrime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if (n % i == 0):
            return False
    return n > 1

def circPrime(n):
    for permutation in circPerm(n):
        if (not isPrime(permutation)):
            return False
    return True


a = input("Enter a number: ")
print("The number {} is{}a circular prime.".format(
    a, ' ' if (circPrime(a)) else ' not '
))
