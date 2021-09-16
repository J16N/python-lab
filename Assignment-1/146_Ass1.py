# 1) Given a string of length greater than 2, return a string except 1 st and last characters.
s = input("Enter a string (Min length > 2): ")
print(s[1:-1])

# 2) Given 2 strings, s1, and s2 return a new string made of the first, middle and last char 
#    each input string.
modify_str = lambda s1, s2: s1[0] + s2[0] + s1[len(s1) // 2] + s2[len(s2) // 2] + s1[-1] + s2[-1]
print( modify_str("abcde", "pqrst") )

# 3) Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
append_to_middle = lambda s, data: s[:len(s) // 2] + data + s[len(s) // 2:]
print( append_to_middle("abcd", "pqrst") )

# 4) Find all occurrences of “India” in given string ignoring the case.
s = input("Enter a string: ")
print(s.count("India"))

# 5) Find the last position of a substring “Emma” in a given string.
s = input("Enter a string: ")
print(s.rfind("Emma"))

# 6) Display the two substring separated by space.
s = input("Enter a string: ")
print(s[:len(s) // 2] + ' ' + s[len(s) // 2:])

# 7) Given an input list removes the element at index 4 and add it to the 2nd position and 
#    also, at the end of the list.
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original List:\n{l}")

el = l.pop(4)
print(f"List after removing element from index-4:\n{l}")

l.insert(2, el)
print(f"List after inserting element at index-2:\n{l}")

l.append(el)
print(f"List after appending element at the end:\n{l}")

# 8) Reverse the following tuple aTuple = (10, 20, 30, 40, 50)
t = (10, 20, 30, 40, 50)
print(t[::-1])

# 9) Access value 20 from the following tuple 
#    aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
t = ("Orange", [10, 20, 30], (5, 15, 25))
print(t[1][1])

# 10) Unpack the following tuple into 4 variables aTuple = (10, 20, 30, 40)
t = (10, 20, 30, 40)
a, b, c, d = t

# 11) Swap the following two tuples tuple1 = (11, 22) tuple2 = (99, 88)
t1 = (11, 22)
t2 = (99, 88)
print(f"t1 = {t1}  |  t2 = {t2}")
t1, t2 = t2, t1
print(f"t1 = {t1}  |  t2 = {t2}")

# 12) Copy element 44 and 55 from the following tuple into a new tuple 
#     tuple1 = (11, 22, 33, 44, 55, 66)
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:-1]

# 13) Modify the first item (22) of a list inside a following tuple to 222 
#     tuple1 = (11, [22, 33], 44, 55)
tuple1 = (11, [22, 33], 44, 55)
print(tuple1)
tuple1[1][0] = 222
print(tuple1)

# 14) Below are the two lists convert it into the dictionary 
# keys = ["Ten", "Twenty", "Thirty"] values = [10, 20, 30]
keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]
print(dict(zip(keys, values)))

# 15) Merge following two Python dictionaries into one 
#     dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} 
#     dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
d = {**dict1, **dict2}
print(d)

# 16) Check if a value 200 exists in a dictionary 
#     sampleDict = {'a': 100, 'b': 200, 'c': 300}
sampleDict = {'a': 100, 'b': 200, 'c': 300}
print( 200 in sampleDict.values() )

# 17) Rename key city to location in the following dictionary
#     sampleDict = { "name": "Kelly", "age": 25, "salary": 8000, "city": "New york" }
sampleDict = { "name": "Kelly", "age": 25, "salary": 8000, "city": "New york" }
sampleDict["location"] = sampleDict.pop("city")
print(sampleDict)

# 18) Get the key corresponding to the minimum value from the following dictionary
#     sampleDict = { 'Physics': 82, 'Math': 65, 'History': 75 }
sampleDict = { 'Physics': 82, 'Math': 65, 'History': 75 }
print( min(sampleDict, key=sampleDict.get) )

# 19) Given a Python dictionary, Change Brad’s salary to 8500
#     sampleDict = { 
#       'emp1': {'name': 'John', 'salary': 7500}, 
#       'emp2': {'name': 'Emma', 'salary': 8000}, 
#       'emp3': {'name': 'Brad', 'salary': 6500} 
#     }

sampleDict = { 
    'emp1': {'name': 'John', 'salary': 7500}, 
    'emp2': {'name': 'Emma', 'salary': 8000}, 
    'emp3': {'name': 'Brad', 'salary': 6500} 
}

print(sampleDict)
sampleDict['emp3']['salary'] = 8500
print(sampleDict)