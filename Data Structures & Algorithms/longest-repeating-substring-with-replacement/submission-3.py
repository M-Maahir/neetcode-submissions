class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hsmp = {}
        res = 0
        l = 0
        maxf = 0 

        for r in range(len(s)):

            hsmp[s[r]] = hsmp.get(s[r], 0)+1
            maxf = max(maxf, hsmp[s[r]])

            if r - l + 1 - maxf <= k:
                res = max(res, r - l + 1)
            else:
                hsmp[s[l]] -= 1
                l += 1
        return res                
        
            

        