class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        new = 0
        i = 0

        if x < 0: return False

        while x:
            mod = x%10
            new = mod + (new*10)
            x = x//10
        
        return True if original == new else False
        