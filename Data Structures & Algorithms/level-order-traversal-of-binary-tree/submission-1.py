# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        curr = root

        q = [curr]
        res = []

        while q and curr:
            lvl = []
            for _ in range(len(q)):
                curr = q.pop(0)
                lvl.append(curr.val)
                if curr:
                    if curr.left: q.append(curr.left)
                    if curr.right: q.append(curr.right)

            if lvl:
                res.append(lvl)
        
        return res


        