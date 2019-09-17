def lowestCommonAncestor(self, root, p, q):
        """
        traversal
        tree searching
        we have to store the parent pointers
        storing node and parent pointer in 
        """
        if root==None: return None
        if root.val==p.val or root.val==q.val: return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if right==None and left==None: return None
        if right!=None and left!=None: return root
        if left!=None: return left
        else: return right


def lowestCommonAncestor(self, root, p, q):
        """
        traversal
        tree searching
        we have to store the parent pointers
        storing node and parent pointer in 
        """
        s = [root]
        p1=False
        q1=False
        s1 = {root:None}#keeping the parent dict
        # print(s)
        while p not in s1 or q not in s1:
            a=s.pop()
            if a.left!=None:
                s1[a.left]=a
                s.append(a.left)
            if a.right!=None:
                s1[a.right]=a
                s.append(a.right)
        a = set()
        while p:
            a.add(p)
            p = s1[p]
        while q not in a:
            q = s1[q]
        return q