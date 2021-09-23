from functools import reduce

product_of_items = lambda l: reduce(lambda x, y: x * y, l)
my_list = map(int, input("Enter the list of numbers (sep by space): ").split())
print("Product of items in the list:", product_of_items(my_list))