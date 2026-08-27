from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = defaultdict(set)
        col = defaultdict(set)
        sqr = defaultdict(set)


        for i in range(9):
            for j in range(9):


                b = board[i][j]

                if b == ".":
                    continue

                if b in row[i] or b in col[j] or b in sqr[(i//3, j//3)]:
                    return False

                
                row[i].add(b)
                col[j].add(b)
                sqr[(i//3, j//3)].add(b)
        
        return True
        