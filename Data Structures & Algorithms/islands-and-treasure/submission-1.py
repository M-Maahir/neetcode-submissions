from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        row = len(grid)
        col = len(grid[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        q = deque()

        visit = set()
        dist = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visit.add((i,j))


        def bfs(r,c):
            if r < 0 or c < 0 or r == row or c == col or grid[r][c] == -1 or (r,c) in visit:
                return 

            visit.add((r,c))
            q.append([r,c])

        
        while q:

            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                for dr, dc in dirs:
                    bfs(dr + r, dc + c)

            dist += 1



        
        




        