def char_type_count(s):
    total_upper_chars = sum(1 for c in s if c.isupper())
    return (total_upper_chars, len(s) - total_upper_chars)

S = input("Enter a string: ")
result = char_type_count(S)
print("Upper case characters:", result[0])
print("Lower case characters:", result[1])