N = int(input("Enter N: "))

print(*reversed(range(1, 2 * N + 1, 2)), sep="\n")
