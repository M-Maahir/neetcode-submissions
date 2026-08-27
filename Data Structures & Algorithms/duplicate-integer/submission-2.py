class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dec = {}

        for i in nums:
            dec[i] = dec.get(i,0)+1

            if dec[i] > 1:
                return True

        return False