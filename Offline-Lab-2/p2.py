a = float(input("Enter a first number: "))
b = float(input("Enter a second number: "))

print("Close" if (abs(a - b) <= 0.001) else "Not close")
