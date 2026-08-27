# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        curr = root

        if curr is None:
            return []

        que = deque([curr])

        while que:
            lvl = []

            for _ in range(len(que)):
                curr = que.popleft()
                lvl.append(curr.val)

                if curr.left: que.append(curr.left)
                if curr.right: que.append(curr.right)

            if lvl:
                res.append(lvl)

        return res
        