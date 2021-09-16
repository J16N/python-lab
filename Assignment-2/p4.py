N = int(input("N: "))

for i in range(1, N + 1):
    row = map(lambda x: 2 ** x, range(i))
    print(*reversed(list(row)), sep=" ")