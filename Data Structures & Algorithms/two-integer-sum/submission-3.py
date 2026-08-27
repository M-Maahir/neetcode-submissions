class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        count = {}

        for i, n in enumerate(nums):
            dif = target - n
            
            if dif in count:
                return [count[dif], i]
            
            count[n] = i
