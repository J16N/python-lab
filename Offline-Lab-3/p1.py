numbers = input("Enter numbers seperated by spaces: ").split()

for number in numbers:
    print("{0} is{1}a palindrome number.".format(
        number, 
        ' ' if (numbers == number[::-1]) else ' not '
    ))
