class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        islands = 0
        row = len(grid)
        col = len(grid[0])


        def bfs(r, c):
            que = []
            que.append((r,c))
            grid[r][c] = "0"

            while que:
                r, c = que.pop()
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nc < 0 or nr >= row or nc >= col or grid[nr][nc] == "0":
                        continue

                    que.append((nr,nc))
                    grid[nr][nc] = "0"

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands
        