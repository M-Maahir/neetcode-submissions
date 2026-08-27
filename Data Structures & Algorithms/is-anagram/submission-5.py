class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sCount = [0]*26

        for i in range(len(s)):
            sCount[ord(s[i]) - ord("a")] += 1
            sCount[ord(t[i]) - ord("a")] -= 1
        
        for i in sCount:
            if i != 0:
                return False
        
        return True
        