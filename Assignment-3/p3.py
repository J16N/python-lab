def product_of_items(l):
    product = 1
    for i in l:
        product *= i
    return product
    
my_list = map(int, input("Enter the list of numbers (sep by space): ").split())
print("Product of items in the list:", product_of_items(my_list))