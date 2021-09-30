from collections import Counter

def reduced_str(s):
    c = Counter(s)
    return ''.join(k for k, v in c.items() if (v % 2 != 0))

S = input("Enter a string: ")
print(reduced_str(S))