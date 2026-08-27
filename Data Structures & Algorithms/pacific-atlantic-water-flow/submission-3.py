class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row = len(heights)
        col = len(heights[0])

        dirs = [[1,0],[-1,0],[0,-1],[0,1]]

        result = []

        pac = set()
        atl = set()

        def dfs(r,c, visit, prv):

            x = (r,c)

            if r < 0 or c < 0 or r == row or c == col or heights[r][c] < prv or x in visit:
                return

            visit.add((r,c))

            for dr, dc in dirs:
                dfs(dr + r, dc + c, visit, heights[r][c])


        for r in range(row):
             dfs(r, 0, pac, heights[r][0])
             dfs(r, col - 1, atl, heights[r][col - 1])

        for c in range(col):
            dfs(0, c, pac, heights[0][c])
            dfs(row - 1, c, atl, heights[row - 1][c])


        for r in range(row):
            for c in range(col):
                x = (r,c)
                if x in pac and x in atl:
                    result.append([r,c])


        return result