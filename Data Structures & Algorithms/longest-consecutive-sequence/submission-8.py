class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        nums = set(nums)

        for i in nums:
            if i - 1 not in nums:
                long = 1
                while i + long in nums:
                    long += 1
                longest = max(longest, long)
        
        return longest
        