from string import ascii_lowercase as lc

is_pangram = lambda s: set(lc) <= set(s)
S = input("Enter a string: ").lower()
print(
    "The given string is",
    " " if is_pangram(S) else " not ",
    "a pangram.",
    sep=""
)