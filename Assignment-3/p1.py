myMax = lambda x, y, z: max(x, y, z)
a, b, c = map(int, input("Enter three numbers (seperated by space): ").split())
print("The maximum number is:", myMax(a, b, c))