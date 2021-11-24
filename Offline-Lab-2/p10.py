nums = list(map(int, input("Enter numbers (seperated by spaces): ").split()))
nums.sort(reverse=True)
print( "Second largest number =", nums[1] )
