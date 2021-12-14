def happy(n):
    if (n == 1 or n == 7):
        return True
    if (n < 10):
        return False
    
    digits = map(int, list(str(n)))
    n = sum(i ** 2 for i in digits)
    return happy(n)

def get_happy_nums(count):
    i, n = 0, 1
    while (i < count):
        if (happy(n)):
            yield n
            i += 1
        n += 1
        

print("The first 10 happy numbers are as follows:")
print(*get_happy_nums(10), sep=', ')
