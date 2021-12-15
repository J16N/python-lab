def chckSym(s):
    if (len(s) % 2):
        return False
        
    mid = len(s) // 2
    return s[:mid] == s[mid:]
    
    
chckPal = lambda s: s == s[::-1]


S = input("Input: ")

print("The '{}' is{}symmetric.".format(
    S, ' ' if (chckSym(S)) else ' not '
))
print("The '{}' is{}palindrome.".format(
    S, ' ' if (chckPal(S)) else ' not '
))
