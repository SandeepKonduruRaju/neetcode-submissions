class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                return self.lowestCommonAncestor(curr.left,p,q)
            elif p.val > curr.val and q.val > curr.val:
                return self.lowestCommonAncestor(curr.right,p,q)
            else:
                return curr