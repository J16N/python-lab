def my_factorial(n):
    return 1 if n == 0 else n * my_factorial(n - 1)
    
N = int(input("Enter a number: "))
print(f"Factorial of {N}:", my_factorial(N))