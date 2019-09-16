# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

# Example 1:

# Input: [1,2,3,4,5]
# Output: true
# Example 2:

# Input: [5,4,3,2,1]
# Output: false

def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        f=s=float('inf')
        for i in nums:
            if i<=f:
                f=i
            elif i<=s:
                s=i
            else:
                return True
            print(s,f)
        return False