# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if subRoot is None:
            return True 
        
        if root is None:
            return False

        if self.dfs(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return (left or right)

    def dfs(self, root, subRoot):

        if root is None and subRoot is None:
            return True

        if root and subRoot and root.val == subRoot.val:
            return (self.dfs(root.left, subRoot.left) and
            self.dfs(root.right, subRoot.right))

        return False
        