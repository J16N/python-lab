autom = lambda num: num == int(str(num ** 2)[-1])

N = int(input("Enter a number: "))
print("The number {} is{}a Automorphic number.".format(
    N, ' ' if (autom(N)) else ' not '
))
