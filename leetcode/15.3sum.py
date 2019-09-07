# Given an array nums of n integers, are there elements 
# a, b, c in nums such that a + b + c = 0? Find all unique 
# triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# def threesum(nums, target):
#     a=[]
#     nums.sort()
#     for i in range(0,len(nums)):
#         target = -nums[i]
#         twoSum(nums[i:], target, [])
#     return a

# def twoSum(nums, target, a):
#     if len(nums) <= 1:
#         return False
#     buff_dict = {}
#     for i in range(len(nums)):
#         if nums[i] in buff_dict:
#             a.append([buff_dict[nums[i]]])
#         else:
#             buff_dict[target - nums[i]] = i
#     print(a)

# The key - use 2sum to simplify the problem - 2 sum can be solved using 2 pointers
b=[]
def threesum(nums, target):
    
    nums = sorted(nums)
    for i in range(0,len(nums)-2):
        target = -nums[i]
        l=i+1
        r=len(nums)-1
        twosum(nums, target, l, r)
            
    print(b)

def twosum(nums, target, l, r):
    while l<r:
        if nums[l]+nums[r]==target:
            k=[]
            k.append(-target)
            k.append(nums[l])
            k.append(nums[r])
            b.append(k)
        l+=1
        r-=1
        while l<r and nums[l]==nums[l-1]:
            l+=1
        while l<r and nums[r]==nums[r+1]:
            r-=1
    return -1

nums = [-1, 0, 1, 2, -1, -4]
target =0
print(threesum(nums, target))
