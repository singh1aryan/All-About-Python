'''

41. first missing positive

Example 1:
HARD Problem - easy solution with sort
Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1

'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 1
        if len(nums)==1:
            if nums[0]==1:
                return 2
            else:
                return 1
            
        nums.sort()
        k=1
        while k<len(nums)+1:
            if k not in nums:
                return k
            k+=1
        return max(nums)+1
    
a = Solution()
print(a.firstMissingPositive([1,2,0]))
print(a.firstMissingPositive([3,4,-1,1]))
print(a.firstMissingPositive([7,8,9,11,12]))

