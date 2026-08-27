class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "": return ""

        l = 0
        resLen = float("inf")
        res = [9, 9]
        have = 0

        countT = {}
        window = {}

        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1
        want = len(countT)

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == want:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                window[s[l]] -=1 

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""        