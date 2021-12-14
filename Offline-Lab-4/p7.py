def harshad(num):
    sumd = sum(map(int, list(str(num))))
    return num % sumd == 0
    

N = int(input("Enter a number: "))
print("The number {} is{}a Harshad number.".format(
    N, ' ' if (harshad(N)) else ' not '
))
