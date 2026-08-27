# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(curr, minV, maxV):
            if curr is None:
                return True

            if not (minV < curr.val and maxV > curr.val):
                return False

            left = dfs(curr.left, minV, curr.val)
            right = dfs(curr.right, curr.val, maxV)

            return left and right

        return dfs(root, float("-inf"), float("inf"))        