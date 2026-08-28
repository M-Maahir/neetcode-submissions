class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0 
        r = len(heights) - 1
        area = 0

        while l <= r:
            minH = min(heights[l], heights[r])
            print(minH)
            area = max(area, minH * (r - l))

            if heights[l] < heights[r]:
                l += 1
            
            else: r -= 1
        
        return area
