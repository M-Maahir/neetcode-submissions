# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        curr = root
        if curr is None:
            return []

        que = deque([curr])
        
        while que:
            for _ in range(len(que)):
                curr = que.popleft()

                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)

            res.append(curr.val)

        return res