'''
771. Jewels and Stones
You're given strings J representing the types of stones
that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels.
'''

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        c=0
        for i in S:
            for j in J:
                if i == j:
                    c+=1
        return c
