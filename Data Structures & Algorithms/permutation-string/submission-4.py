class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        counts1 = [0]*26
        counts2 = [0]*26

        for r in range(len(s1)):
            counts1[ord(s1[r]) - ord('a')] += 1
            counts2[ord(s2[r]) - ord('a')] += 1

        mtch = 0
        for i in range(26):
            if counts1[i] == counts2[i]:
                mtch += 1
        
        l = 0

        for r in range(len(s1), len(s2)):
            if mtch == 26: return True

            idx = ord(s2[r]) - ord('a')
            counts2[idx] += 1

            if counts1[idx] == counts2[idx]:
                mtch += 1
            elif counts1[idx] + 1 == counts2[idx]:
                mtch -= 1
            
            idx = ord(s2[l]) - ord('a')
            counts2[idx] -= 1

            if counts1[idx] == counts2[idx]:
                mtch += 1
            elif counts1[idx] - 1 == counts2[idx]:
                mtch -= 1

            l += 1

        return mtch == 26