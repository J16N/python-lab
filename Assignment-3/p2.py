sum_of_items = lambda l: sum(l)
my_list = map(int, input("Enter the list of numbers (sep by space): ").split())
print("Sum of the list is:", sum_of_items(my_list))