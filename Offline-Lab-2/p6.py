from math import sqrt

def isPrime(n):
	for i in range(2, int(sqrt(n) + 1)):
		if (n % i == 0):
			return False			
	return n > 1
	
isPerfSquare = lambda n: int(sqrt(n)) ** 2 == n
	
N = int(input("Enter a number: "))
print("Square root is" + 
	 (" " if (isPerfSquare(N) and isPrime(sqrt(N))) 
	 else " not ") + "prime."
)
