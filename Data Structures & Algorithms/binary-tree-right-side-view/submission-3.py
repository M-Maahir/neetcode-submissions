# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        que = [root]
        res = []

        while que:
            
            for _ in range(len(que)):
                curr = que.pop(0)
                if curr:
                    if curr.left: que.append(curr.left)
                    if curr.right: que.append(curr.right)

            res.append(curr.val)
            
        return res
        