class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(curr.left,p,q)
            elif p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(curr.right,p,q)
            else:
                return curr