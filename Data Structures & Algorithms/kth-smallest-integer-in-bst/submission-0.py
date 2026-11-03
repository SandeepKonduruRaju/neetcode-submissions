class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = 0
        def inOrder(root):
            nonlocal count,res
            if not root:
                return 0
            inOrder(root.left)
            count += 1
            if count  == k:
                res = root.val
            inOrder(root.right)
        inOrder(root)
        return res