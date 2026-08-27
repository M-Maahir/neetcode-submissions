# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        curr = root
        q = deque([curr])
        n = 0

        while q or curr:
            while curr:
                q.append(curr)
                curr = curr.left

            curr = q.pop()

            n +=1
            if n == k:
                return curr.val
            curr = curr.right
            
            




        