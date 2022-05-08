# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res = collections.deque([root])
        depth = 0
        while res:
            depth += 1
            for i in range(len(res)):
                cur = res.popleft()
                if cur.left:
                    res.append(cur.left)
                if cur.right:
                    res.append(cur.right)
        return depth
            