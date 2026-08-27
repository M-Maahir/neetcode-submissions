class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top = 0
        bot = len(matrix)-1

        l = 0
        r = len(matrix[0])-1

        while top <= bot:
            m = (top + bot)//2

            if target < matrix[m][0]:
                bot = m - 1

            elif target > matrix[m][-1]:
                top = m + 1
            
            else: break

        
        while l <= r:
            mid = (l+r)//2

            if target < matrix[m][mid]:
                r = mid - 1
            
            elif target > matrix[m][mid]:
                l = mid + 1

            else: return True

        return False
        