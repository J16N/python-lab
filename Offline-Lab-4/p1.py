def is_ugly(num):
    prime_factors = [2, 3, 5]
    
    for prime_factor in prime_factors:
        while (num and num % prime_factor == 0):
            num = num / prime_factor
    
    return num == 1 or num == 0


N = int(input("Enter a number: "))
print("The number {} is{}ugly.".format(
    N,
    ' ' if (is_ugly(N)) else ' not '
))
