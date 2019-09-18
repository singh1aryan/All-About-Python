def quicksort(nums):
    if len(nums)<=1:
        return nums
    pivot = nums[len(nums)//2]
    left = [x for x in nums if x<pivot]
    middle = [x for x in nums if x==pivot]
    right = [x for x in nums if x>pivot]
    return quicksort(left)+middle+quicksort(right)


print(quicksort([1,3,4,2,6,5]))

"""
understand the base case, don't just write anything
we divide the array into left,right and middle
then we combine back to form the array again

quicksort - we make left,right and middle arrays and then combine them
we do this recursively but in a sense that we return an array at the end
"""