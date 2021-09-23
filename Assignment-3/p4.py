from math import factorial

my_factorial = lambda n: factorial(n)
N = int(input("Enter a number: "))
print(f"Factorial of {N}:", my_factorial(N))