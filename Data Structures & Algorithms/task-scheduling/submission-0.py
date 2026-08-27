class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        ls = Counter(tasks)
        maxHeap = [-c for c in ls.values()]

        heapq.heapify(maxHeap)
        t = 0
        q = deque()

        while q or maxHeap:
            t += 1

            if not maxHeap:
                t = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, t + n])
            
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return t


         