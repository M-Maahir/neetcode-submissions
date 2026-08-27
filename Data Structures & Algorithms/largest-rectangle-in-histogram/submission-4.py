class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        res = 0
        stack = []

        for idx, h in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > h:
                prvIdx, prvHeight = stack.pop()
                res = max(res, prvHeight*(idx - prvIdx))
                start = prvIdx
            stack.append([start, h])
        
        for i, h in stack:
            res = max(res, h*(len(heights)-i))
        
        return res
        