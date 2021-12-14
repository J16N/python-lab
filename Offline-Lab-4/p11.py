from math import sqrt

def get_prop_div(num):
    divisors = [1]
    for i in range(2, int(sqrt(num) + 1)):
        if (num % i == 0):
            divisors.append(i)
            divisors.append(num / i)
    return divisors

is_amicable = lambda a, b: (
    sum(get_prop_div(a)) == b and
    sum(get_prop_div(b)) == a
)

a, b = map(int, input("Enter 2 numbers (seperated by space): ").split())
print("The two numbers ({}, {}) are{}amicable".format(
    a, b, ' ' if (is_amicable(a, b)) else ' not '
))
