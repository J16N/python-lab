fermet = lambda n: [
    2 ** (2 ** i) + 1
    for i in range(n)
]

print("The first 10 fermet numbers are as follows: ")
print(*fermet(10), sep=', ')
