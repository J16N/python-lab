def duck(num):
    if (num[0] == '0'):
        return False
        
    for d in num:
        if (d == '0'):
            return True
    
    return False
    

N = input("Enter a number: ")
print("The number {} is{}a Duck number.".format(
    N, ' ' if (duck(N)) else ' not '
))
