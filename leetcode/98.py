'''
98. valid BST:
    


'''

def isValidBST(self, root):
    return check_bst(root, float("-inf"), float("inf"))
	
def check_bst(self, node, left, right):
    if not node:
        return True

    if not left < node.val < right:
        return False

    return (check_bst(node.left, left, node.val)
            and check_bst(node.right, node.val, right))
    
'''
Java Code:
    
public boolean isValidBST1(TreeNode root) {
    return isValid(root, null, null);
}

public boolean isValid(TreeNode root, Integer min, Integer max) {
    if(root == null) return true;
    if(min != null && root.val <= min) return false;
    if(max != null && root.val >= max) return false;
    
    return isValid(root.left, min, root.val) && isValid(root.right, root.val, max);
}}

'''