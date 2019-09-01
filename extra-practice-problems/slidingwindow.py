def slidingwindowsum(nums, k):
    max_sum=0
    sliding_sum=0
    # sum for 1st window
    for i in range(0,k):
        sliding_sum+= nums[i]

    for i in range(k, len(nums)):
        sliding_sum+= nums[i]-nums[i-k]
        max_sum = max(max_sum, sliding_sum)

    return max_sum
    

l = [100,200, 100, 600, 100, 100]
print(slidingwindowsum(l, 4)) # returns the max sum of a window of size k=4 here.