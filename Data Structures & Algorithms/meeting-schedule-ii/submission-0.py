"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        res = []
        ans = count = 0

        for i in intervals:
            res.append((i.start, 1))
            res.append((i.end, -1))
        
        res.sort(key= lambda x: (x[0], x[1]))

        for t in res:
            count += t[1]
            ans = max(ans, count)
        
        return ans




        