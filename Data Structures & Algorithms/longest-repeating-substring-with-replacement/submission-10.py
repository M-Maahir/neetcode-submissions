
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hsmp = {}
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            hsmp[s[r]] = hsmp.get(s[r], 0) + 1
            maxf = max(maxf, hsmp[s[r]])

            while r - l + 1 - maxf > k:
                hsmp[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)
        
        return res


