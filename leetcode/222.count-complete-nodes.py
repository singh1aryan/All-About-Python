'''


222. Count Complete Tree Nodes
Medium

966

132

Favorite

Share
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly 
the last, is completely filled, and all nodes in the last 
level are as far left as possible. It can have between 1 
and 2h nodes inclusive at the last level h.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.right == None and root.left == None:
            return 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    