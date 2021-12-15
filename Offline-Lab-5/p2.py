L = filter(
    lambda s: len(s) % 2 == 0, 
    input("Input: ").split()
)


print(*L, sep='\n')
