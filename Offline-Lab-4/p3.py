def kaprekar(start, end):
    numbers = [1]
    
    for i in range(start, end + 1):
        square = str(i ** 2)
        if ( len(square) % 2 == 0 ):
            mid = len(square) // 2
            a, b = int(square[:mid]), int(square[mid:])
            
            if (a + b == i):
                numbers.append(i)
    return numbers
    
print("The Kaprekar numbers between 1 to 1000 are as follows:")
print(*kaprekar(1, 1000), sep=', ')
