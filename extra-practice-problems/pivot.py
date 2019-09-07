# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# The key here is to just notice the condition - when nums[mid]>nums[mid+1] -> mid+1 is the pivot
def pivot(nums):
    if len(nums)==0:
        return -1
    if len(nums)==0:
        return nums[0]
    start =0
    end = len(nums)-1
    # kind of like binary search but finding the smallest element 
    while start <= end:
        mid = (start+end)//2
        print(mid, start, end)
        if nums[mid]>nums[mid+1]:
            return mid+1
        elif nums[start]<= nums[mid]:
            start = mid+1
        else:
            end = mid-1
    return 0

print(pivot([4,5,6,7,0,1,2])) #prints 4 - index for the pivot
print(pivot([5,6,0,1,2,3])) #prints