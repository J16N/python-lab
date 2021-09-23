def char_type_count(s):
    total_upper_chars = total_lower_chars = 0
    for char in s:
        if ('A' <= char <= 'Z'):
            total_upper_chars += 1
        if ('a' <= char <= 'z'):
            total_lower_chars += 1
    
    return (total_upper_chars, total_lower_chars)

S = input("Enter a string: ")
result = char_type_count(S)
print("Upper case characters:", result[0])
print("Lower case characters:", result[1])