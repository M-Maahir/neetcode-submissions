class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for r in range(len(heights)):
            start = r
            while stack and stack[-1][1] > heights[r]:
                pastIdx, pastHeight = stack.pop()
                maxArea = max(maxArea, (r - pastIdx)*pastHeight)
                start = pastIdx
            
            stack.append([start, heights[r]])

        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i)*h)

        return maxArea

        