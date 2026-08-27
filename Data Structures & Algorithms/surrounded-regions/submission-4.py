class Solution:
    def solve(self, board: List[List[str]]) -> None:

        row = len(board)
        col = len(board[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()

        def dfs(r,c):

            if r < 0 or c < 0 or r == row or c == col or board[r][c] != "O" or (r,c) in visit:
                return 

            visit.add((r,c))
            board[r][c] = "T"

            for dr, dc in dirs:
                dfs(dr + r, dc + c)

    

        for r in range(row):
            for c in range(col):
                if (r in (0, row - 1) or c in (0, col - 1)) and board[r][c] == "O":
                    dfs(r,c)
        

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"

        
        for r in range(row):
            for c in range(col):
                if board[r][c] == "T":
                    board[r][c] = "O"