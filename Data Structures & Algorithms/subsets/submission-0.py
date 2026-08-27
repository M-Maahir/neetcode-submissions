class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        rs = []
        subls = []

        def backtrk(i):

            if i == len(nums):
                rs.append(subls.copy())
                return 

            subls.append(nums[i])
            backtrk(i + 1)

            subls.pop()
            backtrk(i + 1)

        backtrk(0)
        return rs