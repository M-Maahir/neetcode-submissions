class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        islands = 0
        row = len(grid)
        col = len(grid[0])


        def dfs(r, c):

            if r < 0 or r == row or c < 0 or c == col or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            for dr, dc in dirs:
                dfs(dr + r, dc + c)


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands

        
