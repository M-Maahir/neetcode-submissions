class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        preEnd = intervals[0][1]
        res = 0

        for start, end in intervals[1:]:

            if start < preEnd:
                preEnd = min(preEnd, end)
                res += 1
            
            else:
                preEnd = end
        
        return res

