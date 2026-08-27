class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        longest = 0

        for i in numset:
            if i - 1 not in numset:
                large = 1
                while i + large in numset:
                    large +=1
                longest = max(longest, large)
                
        return longest

        