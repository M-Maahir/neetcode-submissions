# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0

        def dfs(root = root):

            nonlocal k, res

            if root is None:
                return None
            
            dfs(root.left)

            if k == 0:
                return

            k -= 1
            if k == 0:
                res = root.val

            dfs(root.right)

            return res

        dfs()
        return res
        

        