series = range(1, 43, 3)

print(*series, sep=", ", end="\n")
print(*[i if (i % 2) else -i for i in series], sep=", ", end="\n")
