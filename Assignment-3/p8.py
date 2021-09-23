is_palindrome = lambda s: s == s[::-1]
S = input("Enter a string: ")
print(
    "The given string is",
    " " if is_palindrome(S) else " not ",
    "a palindrome.",
    sep=""
)