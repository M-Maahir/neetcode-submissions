class Solution:
    def minWindow(self, s: str, t: str) -> str:

        window = {}
        count = {}
        have = 0
        resLen = float("inf")
        res = [-1, -1]
        l = 0

        for c in t:
            count[c] = count.get(c, 0)+1

        want = len(count)

        for r in range(len(s)):

            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1

            while have == want:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1

                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res

        return s[l:r+1] if resLen != float("inf") else ""

                

                





        