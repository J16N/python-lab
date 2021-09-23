remove_dup = lambda l: list(set(l))
my_list = map(int, input("Enter the list of numbers (sep by space): ").split())
print("Removing the duplicates: ")
print(*remove_dup(my_list), sep=", ")