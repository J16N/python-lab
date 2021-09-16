is_palindrome = lambda s: s == s[::-1]

S = input("Enter a number: ")
print(f"The number is{' ' if is_palindrome(S) else ' not '}a palindrome")