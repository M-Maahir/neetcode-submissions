class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []
        for x,y in points:
            dist = -(x**2 + y**2)
            heapq.heappush(res, [dist, x, y])
            if len(res) > k:
                heapq.heappop(res)
        

        ans = []
        while res:
            dist, x, y = heapq.heappop(res)
            ans.append([x, y])

        return ans
        