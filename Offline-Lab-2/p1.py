items = int(input("Enter number of items: "))

if (items < 10):
	cost = 120 * items

elif (items >= 10 and items < 100):
	cost = 100 * items
	
else:
	cost = 70 * items
	
print("Total Cost =", cost)
