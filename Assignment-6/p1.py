def starValue(arr, n):
    star = 0
    for i in arr:
        star = star + 1 if (i % n == 0) else star
    return star

def getStarValues(arr): 
    star_values = [starValue(arr[0:i], v) for i, v in enumerate(arr)]
    for a, b in zip(arr, star_values):
        print(f"Star value of {a} = {b}")
    return star_values

num_array = list(map(int, input("Enter the space-seperated number sequence: ").split()))
print(f"Maximum Star Value: { max( getStarValues(num_array) ) }")
