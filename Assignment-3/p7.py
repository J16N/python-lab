is_perfect = lambda N: sum(i for i in range(1, N) if N % i == 0) == N

N = int(input("Enter a number: "))
print(
    "The given number is",
    " " if is_perfect(N) else " not ",
    "a perfect number.",
    sep=""
)