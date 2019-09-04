# Selects the smallest element every time from the remaining elements
# Go through the array once and then select the smallest every other time
# Time complexity - O(N^2) for best, average, and worst case algorithm
# Space complexity - O(1)

def selection(nums):
    for i in range(0,len(nums)):
        min_elem = min(nums[i:])
        for j in range(i+1, len(nums)):
            if nums[j]==min_elem:
                nums[i],nums[j] = nums[j], nums[i]
                break

    return nums

print(selection([1,3,4,5,2,7,3]))
print(selection([1,2,8,5,4,7,3]))
print(selection([1,3,4,8,12,7,3]))