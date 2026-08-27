class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        
        l = 0
        r = 1

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                maxA = prices[r] - prices[l]
                res = max(res, maxA)

            else: l = r

        return res
            
