def lucas(n):
    count = 2
    nums = [2, 1]
    while (count < n):
        nums.append(
            nums[count - 1] + nums[count - 2]
        )
        count += 1
    return nums
    
print("The first 10 Lucas Numbers are as follows:")
print(*lucas(10), sep=', ')
