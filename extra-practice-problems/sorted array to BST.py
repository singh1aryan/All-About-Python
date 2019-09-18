"""

"""

def convert(nums):
    return tree(nums, 0, len(nums)-1)

def tree(nums, l, r):
    if l>r: return None
    mid = (l+r)//2
    node = Node(mid)
    node.left = tree(nums,l,mid-1)
    node.right = tree(nums,mid+1,r)


class Node(object):
    def __init__(self,node):
        self.node=node
        self.left=None
        self.right=None
