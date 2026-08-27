class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False

        s1count = [0]*26
        s2count = [0]*26
        match = 0

        for r in range(len(s1)):
            s1count[ord(s1[r]) - ord("a")] += 1
            s2count[ord(s2[r]) - ord("a")] += 1

        for i in range(26):
            if s1count[i] == s2count[i]:
                match += 1
        
        l = 0 

        for r in range(len(s1), len(s2)):
            if match == 26:
                return True

            idx = ord(s2[r]) - ord("a")

            s2count[idx] += 1

            if s1count[idx] == s2count[idx]:
                match += 1
            elif s1count[idx] + 1 == s2count[idx]:
                match -= 1

            idx = ord(s2[l]) - ord("a")

            s2count[idx] -= 1

            if s1count[idx] == s2count[idx]:
                match += 1
            elif s1count[idx] -1 == s2count[idx]:
                match -= 1

            l += 1

        return match == 26



