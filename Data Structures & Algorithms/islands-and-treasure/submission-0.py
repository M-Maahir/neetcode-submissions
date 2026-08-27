from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        row = len(grid)
        col = len(grid[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        q = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append([r,c])

        
        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c

                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == inf:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append([nr, nc])







        