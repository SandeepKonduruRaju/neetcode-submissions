class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            qlen = len(q) 
            level = []
            for _ in range(qlen):
                node = q.popleft()
                level.append(node.val)
                #print(level)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
            #print("Res",res)
        return res