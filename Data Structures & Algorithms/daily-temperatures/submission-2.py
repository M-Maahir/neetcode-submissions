class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                pastIdx, pastTemp = stack.pop()
                res[pastIdx] = idx - pastIdx
            
            stack.append([idx, temp])

        return res

            