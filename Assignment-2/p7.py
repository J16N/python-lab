from string import ascii_uppercase as letters

def convert(n, base):
    number = []
    while n:
        temp = n % base
        temp = letters[temp - 10] if (temp >= 10) else temp
        number.append(str(temp))
        n = n // base
    return ''.join(number[::-1])

N = int(input("Enter the number: "))
B = int(input("Enter the base: "))
print(f"Converted Number: {convert(N, B)}")