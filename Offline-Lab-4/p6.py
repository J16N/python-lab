def disarium(n):
    digits = list(map(int, list(str(n))))
    return n == sum(digits[i] ** (i + 1) for i in range(len(digits)))
    

N = int(input("Enter a number: "))
print("The number {} is{}a Disarium number.".format(
    N, ' ' if (disarium(N)) else ' not '
))
