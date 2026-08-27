class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top = 0
        bot = len(matrix) - 1

        for i in range(len(matrix)):
            mid = (top + bot)//2

            if target < matrix[mid][0]:
                bot = mid - 1

            elif target > matrix[mid][-1]:
                top = mid + 1 
            
            else: break

        row = mid

        
        l = 0
        r = len(matrix[0])-1

        for i in range(len(matrix[0])):
            mid = (l+r)//2

            if target < matrix[row][mid]:
                r = mid - 1

            elif target > matrix[row][mid]:
                l = mid + 1
            
            else: return True

        return False

        