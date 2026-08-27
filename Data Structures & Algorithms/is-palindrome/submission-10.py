class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s)-1
        s = s.lower()

        def isal(i):
            return (
                ord('a') <= ord(i) <= ord("z") or
                ord('0') <= ord(i) <= ord('9')
                )

        while l < r:

            while l < r and not isal(s[l]): l += 1
            while l < r and not isal(s[r]): r -= 1

            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True    
    
    
        