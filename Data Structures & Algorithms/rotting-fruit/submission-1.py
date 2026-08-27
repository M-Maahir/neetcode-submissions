from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        time = fresh = 0
        q = deque()

        dirs = [[1,0], [-1, 0], [0,1], [0,-1]]

        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append([r,c])

                elif grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            l = len(q)
            for _ in range(l):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr = dr + r
                    nc = dc + c

                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append([nr,nc])

                        fresh -= 1
            time += 1

        
        return time if fresh == 0 else -1






