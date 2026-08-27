class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        l = 0
        r = len(heights)-1

        while l <= r:
            h = min(heights[l], heights[r])
            d = (r - l)

            area = max(area, h*d)

            if heights[l] < heights[r]:
                l += 1
            
            else: r -= 1

        return area
        