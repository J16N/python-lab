pattern = lambda n: [str(i) * (i + 1) for i in range(0, 2 * n, 2)]
R = int(input("Rows: "))
print(*pattern(R), sep='\n')
