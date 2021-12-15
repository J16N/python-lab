L = input("Input: ").split()

capFL = lambda s: s[0].upper() + s[1:-1] + s[-1].upper()
print(' '.join(map(capFL, L)))
