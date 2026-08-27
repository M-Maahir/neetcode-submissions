class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)> len(s2):
            return False 

        a = [0]*26
        b = [0]*26

        mtch = 0
        l = 0

        for i in range(len(s1)):
            a[ord(s1[i]) - ord("a")] += 1
            b[ord(s2[i]) - ord("a")] += 1
        
        for i in range(26):
            if a[i] == b[i]:
                mtch +=1

        for r in range(len(s1), len(s2)):

            if mtch == 26:
                return True

            idx = ord(s2[r]) - ord('a')
            b[idx] += 1

            if b[idx] == a[idx]: mtch += 1
            elif a[idx] + 1 == b[idx]: mtch -= 1

            idx = ord(s2[l]) - ord('a')
            b[idx] -= 1
            if b[idx] == a[idx]: mtch += 1
            elif a[idx] - 1 == b[idx]: mtch -= 1
            l +=1 
        
        return mtch == 26











