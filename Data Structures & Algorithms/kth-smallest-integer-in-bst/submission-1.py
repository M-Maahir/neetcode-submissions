# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0

        def dfs(root):
            nonlocal k
            nonlocal res

            if root is None:
                return
            
            dfs(root.left)
            k -= 1
            if  k == 0:
                res =  root.val
            dfs(root.right)

            return res

        
        return dfs(root)




        