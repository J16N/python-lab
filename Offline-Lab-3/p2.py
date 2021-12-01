# Part 1
seq = [
    ((-1) ** i) * (2 + 3 * i)/(9 + 4 * i)
    for i in range(7)
]

print("Sum =", sum(seq))

# Part 2
mySeq = lambda n: sum(i ** 2 for i in range(1, n + 1, 2))
N = int(input("Enter N: "))
print("Sum = ", mySeq(N))
