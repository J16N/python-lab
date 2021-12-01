from math import pow, factorial

# Part-1
mySeq = lambda n: sum(1 / factorial(i) for i in range(1, n + 1))
N = int(input("Enter n: "))
print("Sum =", 1 + mySeq(N))

# Part-2
otherSeq = lambda x: sum( 
    pow(-1, i - 1) * (x ** i) / factorial(i) 
    for i in range(1, 7)
)

X = int(input("Enter x: "))
print("Sum =", otherSeq(X))
