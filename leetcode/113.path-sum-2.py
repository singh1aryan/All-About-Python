'''

113. Path Sum 2

return all the list of the path sums which equal to target

Given a binary tree and a sum, find all root-to-leaf paths 
where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

'''
# node is the root
p = []
def pathSum2(path, target, node):
    if node is None:
        return
    path.append(node.val)
    if target == node.val and node.right is None and node.left is None:
        path.append(node.val)
        p.append(path)
        return
    else:
        pathSum2(path, target - node.val, node.left)
        pathSum2(path, target - node.val, node.right)
    path = path[:-1]