def insert_all_pos(lst, val):
    new_lst = []
    for i in range(len(lst) + 1):
        temp = lst[:]
        temp.insert(i, val)
        new_lst.append( tuple(temp) )

    return new_lst

L = input("Enter the list (Seperated by space): ").split()
val = input("Enter the value to be inserted: ")

print("Inserting the value at all positions of the list we get: ")
print(*insert_all_pos(L, val), sep='\n')