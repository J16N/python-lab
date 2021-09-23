def myMax(*args):
    max = args[0]
    for i in range(1, len(args)):
        max = max if max > args[i] else args[i]
    return max
    
a, b, c = map(int, input("Enter three numbers (seperated by space): ").split())
print("The maximum number is:", myMax(a, b, c))