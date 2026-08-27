class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        s = [-s for s in stones]
        heapq.heapify(s)

        while len(s) > 1:
            x = heapq.heappop(s)
            y = heapq.heappop(s)

            if x == y:
                continue
            
            if x < y:
                heapq.heappush(s, x - y)
        
        return 0 if not s else -1 * s[0]