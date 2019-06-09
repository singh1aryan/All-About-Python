'''

return the next permutation

Approach:
    get all the permutations and get the one which you want
    problem in this: expensive way to do things
    this is the brute force 
    
we need to know how a permutation works
we have to imagine it as a tree and in the form of a tree

Answer:
    we have to think of this as the reverse and swap question
    we loook for the strictly decreasing section
    we swap the next big number 
    we reverse the whole string
    

'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        # looking for the decreasing section
        while i>=0 and nums[i+1]<=nums[i]:
            i-=1
            
        if i>=0:
            
            j = len(nums)-1
            
            
            while j>=0 and nums[j]<=nums[i]:
                j-=1
                
            nums[i], nums[j] = nums[j], nums[i]
        
        self.reverseNums(nums, i+1)
    
    def reverseNums(self, nums, i):
        left = i
        right = len(nums)-1
        
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
        