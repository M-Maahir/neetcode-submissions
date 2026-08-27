class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []

        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx - 1]:
                continue
            
            l = idx + 1
            r = len(nums)-1
            while l < r:
                sums = num + nums[l] + nums[r]

                if sums < 0:
                    l += 1
                elif sums > 0:
                    r -=1 
                
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res



