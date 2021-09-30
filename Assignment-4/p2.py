reduce_str = lambda s: ''.join( 
    s[i] for i in range(0, len(s)) 
    if (i + 1 == len(s) or s[i] != s[i + 1])
)

def super_reduced(s):
    new_string = reduce_str(s)
    if len(new_string) == len(s):
        return new_string
    return super_reduced(new_string)

s = input("Enter a string: ")
print(super_reduced(s))