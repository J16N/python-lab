def smallest_divisor(n):
    for i in range(2, n):
        if n % i == 0:
            return i
    return n

N = int(input("Enter a number: "))
print("Smallest Divisor: ", smallest_divisor(N))