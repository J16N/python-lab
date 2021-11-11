from itertools import permutations

def isBeautifulPermutation(arr):
    for x, y in zip(arr[:-1], arr[1:]):
        if (x & y == 0):
            return False
    return True

def printBeautifulPermutation(arr):
    for i in arr:
        if (isBeautifulPermutation(i)):
            print(*i, sep=", ", end="\n")

num_array = list(map(int, input("Enter the space-seperated number sequence: ").split()))
printBeautifulPermutation(permutations(num_array))
