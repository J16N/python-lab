get_sorted_str = lambda s: '-'.join(sorted(s.split('-')))

S = input("Enter hyphen seperated sequence of words: ")
print("After Sorting: ")
print(get_sorted_str(S))