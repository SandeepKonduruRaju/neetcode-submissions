class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        bigsum = float('-inf')
        def findsum(root):
            nonlocal bigsum
            if not root:
                return 0
            lsum = max(findsum(root.left),0)
            rsum = max(findsum(root.right),0)
            bigsum = max(bigsum, lsum+rsum+root.val)
            return (root.val + max(lsum,rsum))

        findsum(root)
        return bigsum
        