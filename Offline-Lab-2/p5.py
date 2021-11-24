m = int(input("Enter m: "))
n = int(input("Enter n: "))

for i in range(m, n + 1, m):
	print(i, "is divisible by", m)
	print(i, "is", "odd" if (i % 2) else "even")
