from string import ascii_uppercase as au

pattern = lambda n: [au[i-1:i] * i for i in range(1, n + 1)]
R = int(input("Rows:"))
print(*pattern(R), sep='\n')
