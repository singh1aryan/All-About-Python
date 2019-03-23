# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 02:13:45 2019

@author: Aryan Singh
"""

'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf node.

'''

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            if left > right:
                return left+1
            else:
                return right+1
            
'''
2nd approach
Using max function, 1 liner
'''

def maxDepth1(root):
    if root is None:
        return 0
    else:
        return 1 + max(maxDepth1(root.left),maxDepth1(root.right))
            