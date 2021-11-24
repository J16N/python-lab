a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if (a == b == c):
	type = "Equilateral"

elif (a == b or b == c or c == a):
	type = "Isoceles"
	
else:
	type = "Scalene"
	
print(type, "Triangle")
