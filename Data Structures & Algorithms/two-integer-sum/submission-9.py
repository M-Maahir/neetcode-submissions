class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hsmp = {}

        for i in range(len(nums)):
            n = target - nums[i]
            if n in hsmp:
                return [hsmp[n], i]
            hsmp[nums[i]] = i  

