class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []

        ls = []
        for x, y in points:
            temp = (x)**2 + y**2
            ls.append([temp, (x,y)])

        heapq.heapify(ls)

        while k != 0:

            res.append(heapq.heappop(ls)[1])
            k -= 1

        return res


        
