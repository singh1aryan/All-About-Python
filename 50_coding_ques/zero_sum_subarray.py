
"""
find subarray with sum=0

first take is brute force, take all subarrays and find
we might be able to do something with 2 pointers
max substring window might help
first thought -> 2 pointers from the starting, shifting one another
dp - probably not or maybe yes - using 1d matrix

solution - 
1. simple check if prefix is repeating or the sum==0
2. make a dp 2d array, add dp[i-1] + nums[i] to dp[i] and check if you have a 0 or not
"""

# def subarray(nums):
#     dp = [[0]]*len(nums)
#     dp[0]=[nums[0]]
#     print(dp)
#     for i in range(1,len(nums)):
#         for j in dp[i-1]:
#             dp[i].append(j+nums[i])
#     print(dp)
# subarray([1,2,-5,1,2,-1])

def subarray(nums):
    s = set()
    sum=0
    for i in range(0,len(nums)):
        sum+=nums[i]
        if sum==0 or sum in s:
            return True
        s.add(sum)
  	print(s)
  	# return False

print(subarray([1,2,-5,1,2,-1]))
print(subarray([-1,-2,5, -3]))
