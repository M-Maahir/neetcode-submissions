class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        dirs = [[1,0], [-1,0],[0,1],[0, -1]]
        row = len(grid)
        col = len(grid[0])

        maxArea = 0

        def dfs(r, c):

            if r < 0 or c < 0 or r == row or c == col or grid[r][c] == 0:
                return 0

            area = 1
            grid[r][c] = 0

            for dr, dc in dirs:
                area += dfs(dr + r, dc + c)
            
            return area

        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea