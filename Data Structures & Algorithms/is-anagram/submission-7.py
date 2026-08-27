class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count = [0]*26

        if len(s) != len(t):
            return False
        
        for r in range(len(s)):
            count[ord(s[r]) - ord('a')] += 1
            count[ord(t[r]) - ord('a')] -= 1

        for i in count:
            if i != 0:
                return False
        return True 
        