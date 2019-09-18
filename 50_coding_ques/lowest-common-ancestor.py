"""
famous question - find the lca
 - recursive - passing value bottom up
 - iterative - making a parents dictionary and using that

"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lca(root, p, q):
    s=[root]
    b = {root: None} # node-parent dictionary
    while p not in b or q not in b:
        a = s.pop() 
        if a.left!=None:
            b[a.left]=a
            s.append(a.left)
        if a.right!=None:
            b[a.right]=a
            s.append(a.right)
    print(b)
    a=set()
    while p:
        a.add(p) # add it to the set
        p=b[p] # walk up - make this the parent node
    while q not in a:
        q=b[q]
    return q

# p = TreeNode{val: 5, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 2, left: TreeNode{val: 7, left: None, right: None}, right: TreeNode{val: 4, left: None, right: None}}}
# q = TreeNode{val: 1, left: TreeNode{val: 0, left: None, right: None}, right: TreeNode{val: 8, left: None, right: None}}
# root = TreeNode{val: 3, left: TreeNode{val: 5, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 2, left: TreeNode{val: 7, left: None, right: None}, right: TreeNode{val: 4, left: None, right: None}}}, right: TreeNode{val: 1, left: TreeNode{val: 0, left: None, right: None}, right: TreeNode{val: 8, left: None, right: None}}}
# lca(root,p,q)