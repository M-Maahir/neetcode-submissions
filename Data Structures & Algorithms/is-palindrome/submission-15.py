class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        def isA(l):
            return ord("a") <= ord(l) <= ord("z") or ord("0") <= ord(l) <= ord("9")

        l = 0
        r = len(s) - 1
        
        while l < r:

            while l < r and not isA(s[l]):
                l += 1
            
            while l < r and not isA(s[r]):
                r -= 1
            
            if s[l] != s[r]: return False
        
            l += 1
            r -= 1
        
        return True




        