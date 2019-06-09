'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

concept:
    
test cases:
    
recursive vs iterative:
    
'''
import math
import itertools
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(itertools.permutations(nums))
    
  
''' without itertools, recursive, loops'''
def dfs(nums, array, answer):
    if len(array) == len(nums):
        #print(array)
        answer.append(array)
        if len(answer) == 2:
            print(answer)
            return answer
    else:    
        for i in range(0,len(nums)):
            if nums[i] in array:
                continue
            array.append(nums[i])
            dfs(nums, array, answer)
            array.pop()
    
a = []
b = dfs([1,2],[],a)
print(a)
print(b)