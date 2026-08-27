class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hsmp = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hsmp:
                return [hsmp[diff], i]
            
            hsmp[nums[i]] = i 
    
        