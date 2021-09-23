def sum_of_items(l):
    sum = 0
    for i in l:
        sum += i
    return sum

my_list = map(int, input("Enter the list of numbers (sep by space): ").split())
print("Sum of the list is:", sum_of_items(my_list))