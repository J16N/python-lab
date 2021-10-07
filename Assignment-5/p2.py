def max_neighbour(S):
    curr, count, max_n = S[0], 0, 0
    for i in S:
        if (i == curr):
            count += 1

        else:
            max_n = max(max_n, count)
            count = 1

        curr = i
    
    return max_n

S = input("Enter the string: ")
print("The maximum length of the neighbour is: ", max_neighbour(S))