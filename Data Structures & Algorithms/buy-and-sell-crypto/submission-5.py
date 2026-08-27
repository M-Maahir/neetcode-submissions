class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 0
        res = 0

        while r < len(prices):
            while prices[l] > prices[r]:
                l += 1
            if prices[r] > prices[l]:
                res = max(res ,prices[r] - prices[l])
            r+=1
        return res
        