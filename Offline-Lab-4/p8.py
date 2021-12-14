from math import sqrt

pronic = lambda num: num == int(sqrt(num)) * int(sqrt(num) + 1)

N = int(input("Enter a number: "))
print("The number {} is{}a Pronic number.".format(
    N, ' ' if (pronic(N)) else ' not '
))
