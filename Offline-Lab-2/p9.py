N = int(input("Enter number ( > 20 ): "))

for i in range(11, N + 1):
	print(i, end=" ")
	print("Tipsy" if (i % 3 == 0) else "", end="")
	print("Topsy" if (i % 7 == 0) else "")
